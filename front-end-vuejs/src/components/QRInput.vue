<template>
    <div class="wrapper">
        <div class="title">
            <h2>QR Code Generator</h2>
        </div>
        <div class="input-bar">
            <div class="text_input">
                <input type="url" v-model="textInput" id="text" placeholder="Enter text here" @keyup.enter="sendInput" required />
                <button @click="sendInput">Submit</button>
            </div>
        </div>
    </div>
    
</template>

<script>
/*sendInput fxn*/
 /** textInput variable which receives input */
 export default {
    data () {
        return {
            textInput: '',
            qrUrlChild: '', //URL of QR Code image in Input Child Component
            currentDateTime: ''
        };
    },
    methods: {
        
        formatTime() {
            let now = new Date();
            let day = now.getHours().toString().padStart(2, '0');
            let minutes = now.getMinutes().toString().padStart(2, '0');
            let seconds = now.getSeconds().toString().padStart(2, '0');
            this.currentDateTime = `${day}${minutes}${seconds}`
            },
        sendInput(){
            this.formatTime()
            fetch(`http://api.qrcode.ebamforesume.cloud:8000?url=${this.textInput}&dateTime=${this.currentDateTime}`, {
                method: 'GET',
                headers: {
                    "accept": "application/json", 
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ');
                }
                    return response.json();
            })
            .then(jsonResponse => {

                // Access elements of the JSON response and assign to variables
                this.qrUrlChild = jsonResponse.qrurl;
                console.log(this.qrUrlChild)

                if (this.qrUrlChild.length !== 0) {
                //This enables the Download button if a URL is returned from POST Request
                this.$emit('enableButton');

                //assign qrUrlChild variable to URL received from API POST request
                //This emits the URL of the QR-Code received to the App.vue component to be send to QROutput component
                this.$emit('updateUrl', this.qrUrlChild);
            }})
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
        }
    }
 }
</script>

<style scoped>
.wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 2px auto;
    padding: 10px;
    border: 0px solid;
    border-color: black;
    border-radius: 20px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px, rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
    background-color: rgba(245, 245, 245, 0.596);
    width: 500px;  
}

.wrapper .title h2{
    font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 6px;
}

.text_input input {
    height: 32px;
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    border: 2px solid;
    border-right: 0;
    border-color: #2c3e508e; 
    width: 300px;
}

.text_input {
    box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

/* Apply styles when the input box is focused */
.text_input input:focus {
  border-color: #2c3e508e; /* Change border color */
  box-shadow: 0 0 8px rgba(102, 175, 233, 0.6); /* Add a shadow for better visibility */
  outline: none; /* Remove the default outline */
}

button {
    background: #2c3e508e;
    border: 2px solid;
    padding: 10px 20px;
    padding-bottom: 9px;
    border-color: #2c3e5086;
    margin-top: 0px;
    color: white;
    border-radius: 10px;
    text-align: center;
    font-weight: 700;
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 13px;
    transition: all 0.1s ease;
}

button:hover {
    border: 2px solid;
    background: #2c3e50e0;
    border-color:  #2c3e5086;
    cursor: pointer;
}

button:active{
    background: #2c3e50e0;
    border: 2px solid;
    border-color:  #2c3e5086;
    cursor: progress;
}

input {
    padding-left: 10px;
}
</style>