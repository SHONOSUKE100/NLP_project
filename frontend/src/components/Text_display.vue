<!-- text-display.vue -->
<template>
  <v-main class="">
    <v-container>
      <v-btn @click="fetchResult">Fetch Result</v-btn>
      <div v-if="result">{{ result }}</div>
    </v-container>
  </v-main>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'TextDisplay',
  data() {
    return {
      result: null
    };
  },
  methods: {
    fetchResult() {
      axios.post('http://localhost:8000/api/get_processed_text/', {
        // 任意の条件などを送信できます
      })
      .then(response => {
        this.result = response.data.result;
      })
      .catch(error => {
        console.error('An error occurred:', error);
        console.log('Error Data:', error.response.data);
        console.log('Error Status:', error.response.status);
        console.log('Error Headers:', error.response.headers);
      });
    }
  },
  mounted() {
    this.fetchResult();
  }
}
</script>
  
  