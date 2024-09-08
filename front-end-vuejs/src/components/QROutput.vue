<template>
    <div class="container">
        <div class="wrapper" id="wrapper">
        <div v-if="dlButton">
            <img alt="Generic Stuff" :src="qrUrl">
        </div>
        <div v-else>
            <img alt="QR Code" :src="qrUrl">
        </div>
    </div>
    <div class="dl-button" >
            <a :href="qrUrl" download>
                <button :disabled='!dlButton' @click="downloadPhoto">Download</button>
            </a>
        </div>
    </div>   
</template>

<script>
export default {

    //dlButton props enables download button and 
    //also changes the image from default image to the QR Code
    props: ['qrUrl', 'dlButton'],
    data () {
        return {
            //genericImage: require('@/assets/placeholder.png'),
            //imageSrc: this.qrUrl
        }
    },
   /* watch: {
        qrUrl: {
            handler(val) {

                if (val !== 0){
                    this.qrUrl=val
                }
                else {
                    this.qrUrl = '@/assets/baah.jpeg'
                }
                //return (val !== 0) ? require(val) : require('@/assets/baah.jpeg')
            }
            
        }
    },*/
    methods: {
        downloadPhoto () {
            //Use link in qrUrl prop to generate download link
            
            console.log('Image Downloaded', this.qrPresent)
            console.log('abc',this.qrUrl)
            console.log('Download Button status',this.dlButton)
        },
        /*imgUrl (){
            //console.log('imgURL',this.qrUrl)
            return (this.qrUrl.length !== 0) ? require(this.qrUrl) : require('@/assets/baah.jpeg')
        }*/
    }    
  }

</script>


<style scoped>

.wrapper {
    display: flex;
    border: 0px solid;
    border-color: #4489f1;
    border-radius: 20px;
    box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 1px, rgba(0, 0, 0, 0.07) 0px 2px 2px, rgba(0, 0, 0, 0.07) 0px 4px 4px, rgba(0, 0, 0, 0.07) 0px 8px 8px, rgba(0, 0, 0, 0.07) 0px 16px 16px;
    background-color:  #2c3e508e;
    padding: 10px;
    padding-bottom: 0;
    height: 400px;
    width: 500px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    margin: 2px;
    justify-content: center;
    align-items: center;
}

img {
  width: 350px;
  height: 350px;
  margin: 0px;
  padding: 0;
  border-radius: 10px;
  
}

.dl-button button{
    border-radius: 12px;
    border: 2px solid;
    background: #2c3e505b;
    border-color: #2c3e508e;
    cursor: pointer;
    color: white;
    font-weight: 700;
    font-family: 'Helvetica', 'Arial', sans-serif;
    padding: 10px 20px;
    margin-top: 10px;
    transition: all 0.2s ease;
}

.dl-button button:hover {
    border-radius: 12px;
    border: 2px solid;
    background: #2c3e508e;
    border-color: black;
    cursor: pointer;
    color: white;
    margin-top: 10px;
    font-weight: 700;
    font-family: 'Helvetica', 'Arial', sans-serif;
    padding: 10px 20px;
}

.dl-button button:disabled, .dl-button button[disabled]{
    border-radius: 12px;
    border: 2px solid;
    border-color: #2c3e508e;
    padding: 10px 20px;
    background-color: whitesmoke;
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-weight: 700;
    margin-top: 10px;
    color: gray;
    cursor: not-allowed;
}

</style>