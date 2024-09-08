resource "local_file" "kubeconfig" {
  depends_on = [azurerm_kubernetes_cluster.aks-cluster01]
  filename   = "config"
  content    = azurerm_kubernetes_cluster.aks-cluster01.kube_config_raw
}

output "client_id" {
  value = azurerm_kubernetes_cluster.aks-cluster01.key_vault_secrets_provider[0].secret_identity[0].client_id
}

output "tenant_id" {
  value = azurerm_key_vault.akv-01.tenant_id
}