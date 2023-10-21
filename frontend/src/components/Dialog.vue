<template>
    <!-- <v-chip :color="getColorLabel(item.label)" @mouseenter="showModal = true" @mouseleave="showModal = false">{{ item.word }}</v-chip> -->
    <v-chip :color="getColorLabel(item.label)" @click="showModal = true">{{ item.word }}</v-chip>
    
    <v-dialog v-model="showModal" max-width="600px">
      <v-card>
        <v-card-title>Entity Details</v-card-title>
        <v-card-text>
          <!-- モーダル内のコンテンツをカスタマイズ -->
          <span v-if="item.label === 'None'">
            Word: {{ item.word }}
          </span>
          <span v-else>
            <v-img v-if="imageUrl === null" src="../assets/no-image.png" alt="no-image"></v-img>
            <v-img v-else :src="imageUrl" alt="image"></v-img>
            Label: {{ item.label }}
            Word: {{ item.word }}
          </span>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="showModal = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import ColorLabel from './color';
import axios from 'axios';
export default {
  props: {
    item: Object 
  },
  data() {
    return {
      showModal: false,
      imageUrl: null
    };
  },
  methods: {
    getColorLabel(label) {
      // ラベルに対応する色を返すメソッド
      return ColorLabel[label] || 'orange'; // ラベルが定義されていない場合は 'orange'
    },
    getImage(value){
      const API_KEY = "40185227-1a1325527079599bcc211f6bf";
      const baseUrl = 'https://pixabay.com/api/?key=' + API_KEY;
      var keyword = '&q=' + encodeURIComponent( value );
      var option = '&orientation=horizontal';
      var URL = baseUrl + keyword + option;
      axios.get(URL, {
        // 任意の条件などを送信できます
      })
        .then(response => {
          this.imageUrl = response.data.hits[0].webformatURL;
          console.log(this.imageUrl);
        })
        .catch(error => {
          console.error('An error occurred:', error);
          console.log('Error Data:', error.response.data);
          console.log('Error Status:', error.response.status);
          console.log('Error Headers:', error.response.headers);
        });
      }
    },
  mounted(){
    this.getImage(this.item.word);
  }
};
</script>
