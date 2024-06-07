<template>
  <!-- <v-chip :color="getColorLabel(item.label)" @mouseenter="showModal = true" @mouseleave="showModal = false">{{ item.word }}</v-chip> -->
  <v-chip :color="getColorLabel(item.label)" @click="showModal = true">{{ item.word }}</v-chip>

  <v-dialog v-model="showModal" max-width="600px">
    <v-card>
      <v-card-title>Entity Details</v-card-title>
      <v-card-text>
        <!-- モーダル内のコンテンツをカスタマイズ -->
        <v-img v-if="imageUrl !== null" :src="imageUrl" alt="image" class="responsive-image">
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
            </v-row>
          </template>
        </v-img>
        <v-img v-else src="https://www.shoshinsha-design.com/wp-content/uploads/2020/05/noimage-760x460.png">
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
            </v-row>
          </template>
        </v-img>
        <p>Word: {{ item.label }}</p>
        <p>Label: {{ item.word }}</p>
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
  name: 'Dialog',
  props: {
    item: Object
  },
  data() {
    return {
      showModal: false,
      imageUrl: '',
    };
  },
  methods: {
    getColorLabel(label) {
      // ラベルに対応する色を返すメソッド
      return ColorLabel[label] || 'orange'; // ラベルが定義されていない場合は 'orange'
    },
    getImage(value) {
      const API_KEY = prosess.env.API_KEY;
      const baseUrl = 'https://pixabay.com/api/?key=' + API_KEY;
      var keyword = '&q=' + encodeURIComponent(value);
      var option = '&orientation=horizontal';
      var URL = baseUrl + keyword + option;
      axios.get(URL, {
        // 任意の条件などを送信できます
      })
        .then(response => {
          if (response.data.hits.length > 0) {
            // ランダムなインデックスを生成
            const randomIndex = Math.floor(Math.random() * response.data.hits.length);
            // ランダムに選択した画像のURLを設定
            this.imageUrl = response.data.hits[randomIndex].webformatURL;
          } else {
            // 検索結果が0の場合、デフォルトの画像を表示
            this.imageUrl = null;
            console.log("no-image");
          }
        })
        .catch(error => {
          console.error('An error occurred:', error);
        })
        .finally(() => {

        });
    },
    noImage() {
      this.imageUrl = require("@/public/no-image.png");
    },
  },
  mounted() {
    this.getImage(this.item.word);
  }
};
</script>
