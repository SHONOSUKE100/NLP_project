<!-- text-display.vue -->
<template>
  <v-main class="">
    <v-container>
      <div v-if="result">
        <span v-for="(item, index) in result.text" :key="index">
          <span v-if="item.label === 'None'">
            {{ item.word }}&nbsp
          </span>
          <span v-else>
            <Dialog :item="item"></Dialog>&nbsp
          </span>
        </span>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import axios from 'axios';
import Dialog from './Dialog.vue';


export default {
  name: 'TextDisplay',
  data() {
    return {
      result: null,
      showModal: false,
    };
  },
  components: {
    Dialog
  },
  methods: {
    fetchResult() {
      axios.get('http://localhost:8000/api/processed_with_rulebase/', {
        // 任意の条件などを送信できます
      })
        .then(response => {
          this.result = response.data.result;
          console.log(this.result);
        })
        .catch(error => {
          console.error('An error occurred:', error);
          console.log('Error Data:', error.response.data);
          console.log('Error Status:', error.response.status);
          console.log('Error Headers:', error.response.headers);
        });
    },
  },
  mounted() {
    this.fetchResult();
  }
}
</script>
