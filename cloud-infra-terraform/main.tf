resource "azurerm_resource_group" "rg" {
  name     = "rg-project-qr-code"
  location = "eastus"

  tags = {
    environment = "production"
    project     = "qr-code"
  }
}

data "azurerm_client_config" "current" {}

resource "azurerm_storage_account" "storage-account01" {
  name                     = "qrcode80335"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "production"
    project     = "qr-code"
  }
}

resource "azurerm_storage_management_policy" "lifecycle-policy-01" {
  storage_account_id = azurerm_storage_account.storage-account01.id

  rule {
    name    = "delete-after-1-day"
    enabled = true
    filters {
      blob_types = ["blockBlob", "appendBlob"]
    }
    actions {
      base_blob {
        delete_after_days_since_creation_greater_than = 1
      }
    }
  }

  depends_on = [azurerm_storage_account.storage-account01]
}

resource "azurerm_kubernetes_cluster" "aks-cluster01" {
  name                = "aks-cluster01"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "akscluster01"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_B2s"
  }
  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin    = "kubenet"
    load_balancer_sku = "basic"
  }
  tags = {
    environment = "production"
    project     = "qr-code"
  }

  key_vault_secrets_provider {
    secret_rotation_enabled = true
  }

}

resource "azurerm_key_vault" "akv-01" {
  name                        = "akv-01-qr80335"
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 30
  purge_protection_enabled    = false
  sku_name                    = "standard"

  depends_on = [azurerm_kubernetes_cluster.aks-cluster01]

  tags = {
    environment = "production"
    project     = "qr-code"
  }
}

resource "azurerm_key_vault_secret" "azure-storage-connection-string" {
  name         = "AZURESTORAGECONNECTIONSTRINGQR"
  value        = azurerm_storage_account.storage-account01.primary_blob_connection_string
  key_vault_id = azurerm_key_vault.akv-01.id
  depends_on   = [azurerm_key_vault_access_policy.vault-access-policy-01, azurerm_key_vault_access_policy.vault-access-policy-02]
}

resource "azurerm_key_vault_access_policy" "vault-access-policy-01" {
  key_vault_id = azurerm_key_vault.akv-01.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_kubernetes_cluster.aks-cluster01.key_vault_secrets_provider[0].secret_identity[0].object_id

  secret_permissions = [
    "Get", "List",
  ]
  depends_on = [azurerm_kubernetes_cluster.aks-cluster01]
}

resource "azurerm_key_vault_access_policy" "vault-access-policy-02" {
  key_vault_id = azurerm_key_vault.akv-01.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = [
    "Set",
    "Get",
    "List",
    "Delete",
    "Purge",
    "Recover"
  ]
  depends_on = [azurerm_kubernetes_cluster.aks-cluster01]
}

