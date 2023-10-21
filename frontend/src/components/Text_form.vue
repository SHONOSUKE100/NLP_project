<template>
  <v-footer color="blue-grey-lighten-5" app>
    <v-row no-gutters>
      <v-col cols="11">
        <v-textarea class="custom-textarea" ref="textarea" v-model="text" @input="handleInput"></v-textarea>
      </v-col>
      <v-col cols="1" class="d-flex" align-center>
        <v-btn class="h-50 " @click="send" large rounded color="blue-grey-lighten-5" :elevation="3">
          <v-icon left>mdi-send</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Form',
  data(){
    return {
      text: ''
    }
  },
  mounted() {
    this.initializeHeight();
  },
  methods: {
    send() {
      axios.post('http://localhost:8000/api/process/', {
        text: this.text
      })
      .then(response => {
        console.log('Message sent:', response.data);
        this.text = ''
        
      })
      .catch(error => {
        console.error('An error occurred:', error);
        console.log('Error Data:', error.response.data);
        console.log('Error Status:', error.response.status);
        console.log('Error Headers:', error.response.headers);
      });
      this.$emit("dataSubmitted");
    },
    initializeHeight() {
      const textarea = this.$refs.textarea.$el.querySelector("textarea");
      const lineHeight = parseFloat(window.getComputedStyle(textarea)["line-height"]);
      textarea.style.height = `${lineHeight}px`;  // 1行分の高さに設定
    },
    handleInput() {
      this.$nextTick(() => {
        const textarea = this.$refs.textarea.$el.querySelector("textarea");
        const lineHeight = parseFloat(window.getComputedStyle(textarea)["line-height"]);
        const maxLines = 5;
        let lineCount = textarea.value.split(/\r\n|\r|\n/).length;

        if (lineCount > maxLines) {
          textarea.style.overflowY = "auto";
          textarea.style.height = `${lineHeight * maxLines}px`;
        } else {
          textarea.style.overflowY = "hidden";
          textarea.style.height = `${lineHeight * lineCount}px`;  // 行数に合わせて高さを調整
        }
      });
    },
  },
}
</script>

<style>
.custom-textarea textarea {
  overflow-y: hidden; 
}
</style>
