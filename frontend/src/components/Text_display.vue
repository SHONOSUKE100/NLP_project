<!-- text-display.vue -->
<template>
  <v-main class="">
    <v-container>
      <div class="text-center">
        
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props">
              Model
            </v-btn>
          </template>
          <v-list @click:select="clickItem">
            <v-list-item key="1" value="1">
              <v-list-item-title>Model1</v-list-item-title>
            </v-list-item>
            <v-list-item key="2" value="2">
              <v-list-item-title>Model2</v-list-item-title>
            </v-list-item>
            <v-list-item key="3" value="3">
              <v-list-item-title>Model3</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
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
import { ref } from 'vue';

export default {
  name: 'TextDisplay',
  setup() {
    const url = ref('http://localhost:8000/api/get_processed_text/');
  },
  data() {
    return {
      result: null,
      showModal: false,
      selected: '',
      url: "http://localhost:8000/api/get_processed_text/",
      endpoints: [
        {id: 1, name: 'model1',url: "http://localhost:8000/api/get_processed_text/"},
        {id: 2, name: 'model2', url: "aaaa"},
        {id: 3, name: 'model3', url: "a"},
      ]
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
    clickItem(event){
      this.selected = event.id;
    }
  },
  mounted() {
    this.fetchResult();
  }
}
</script>
