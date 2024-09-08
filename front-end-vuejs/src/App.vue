<template>  
    <div class="background">
      <QRInput @updateUrl="urlUpdate" @enableButton="enableDownloadButton"/>
      <QROutput :qrUrl= "qrUrlParent" :dlButton="downloadButton"/>
    </div> 
</template>


<script>
import QRInput from './components/QRInput.vue'
import QROutput from './components/QROutput.vue'

export default {
  name: 'App',
  components: { QRInput, QROutput },

  data (){
    return {
      qrUrlParent: require('@/assets/placeholder.png'), //URL of blob storage of URL generated
      downloadButton: false
    };
  },
  methods: {
    urlUpdate (urlGen) {
      /**This function updates qrUrlParent with the data gotten from qrUrlChild form QRInput Component ie urlGen*/
      console.log('hello',urlGen);
      this.qrUrlParent = urlGen;
    },

    //This function enables download button and also changes image from generic image to blob storage of URL image
    enableDownloadButton(){
      this.downloadButton = true;
    }
  }
}
</script>


<style >
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 6px;
  background-color: #b4b5b800;
}

.background{
    background-color: lightgrey;
    background-image: none;
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    z-index: -1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center; 
}

</style>
