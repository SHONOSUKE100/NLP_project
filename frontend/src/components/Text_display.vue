<!-- text-display.vue -->
<template>
  <v-main class="">
    <v-container>
      <v-btn @click="fetchResult">Fetch Result</v-btn>
      <div v-if="result">
        <span v-for="(item, index) in result.text" :key="index">
          <span v-if="item.label === 'None'">
            <span>{{ item.word }}</span>
          </span>
          <v-chip v-else :color="getColorLabel(item.label)">{{ item.word }} </v-chip>&nbsp
        </span>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import axios from 'axios';
import Dialog from './dialog.vue';
import ColorLabel from './color';

export default {
  name: 'TextDisplay',
  data() {
    return {
      result: null,
    };
  },
  components: {
    Dialog
  },
  methods: {
    fetchResult() {
      axios.post('http://localhost:8000/api/get_processed_text/', {
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
    getColorLabel(label) {
      // ラベルに対応する色を返すメソッド
      return ColorLabel[label] || 'orange'; // ラベルが定義されていない場合は 'orange'
    }
  },
  mounted() {
    this.fetchResult();
  }
}
</script>
