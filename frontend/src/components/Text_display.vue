<!-- text-display.vue -->
<template>
  <v-main class="">
    <v-container>
      <v-btn @click="fetchResult">Fetch Result</v-btn>
      <div v-if=this.$store.state.send v-html="highlightedText"></div>
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
  computed: {
    send () {
      return this.$store.state.send
    }
  },
  methods: {
    fetchResult() {
      axios.post('http://localhost:8000/api/get_processed_text/', {
        // 任意の条件などを送信できます
      })
        .then(response => {
          this.result = response.data.result;
          this.highlightText();
        })
        .catch(error => {
          console.error('An error occurred:', error);
          console.log('Error Data:', error.response.data);
          console.log('Error Status:', error.response.status);
          console.log('Error Headers:', error.response.headers);
        });
    },
      highlightText() {
        if (this.result) {
          const Data = this.result; // JSONデータを解析
          console.log(Data);
          let highlightedText = ''; // ハイライトされたテキスト
    
          // テキスト内の各単語に対して処理
          const words = Data.entities; // 単語の位置情報を含む配列
          console.log(words);
          for (let i = 0; i < words.length; i++) {
            const wordData = words[i];
            const label = wordData.label; // ラベル (e.g., "PERSON")
            const word = wordData.word; // 単語
    
            // ハイライトスタイルを設定
            const highlightStyle = `background-color: yellow; display: inline-block;`;
    
            // ラベルによってスタイルをカスタマイズ (必要に応じて)
            if (label === 'PERSON') {
              // 人物の名前の場合、特定のスタイルを適用
            }
    
            // ハイライトされたテキストを生成
            highlightedText += `<span style="${highlightStyle}">${word}</span> `;
          }
    
          this.highlightedText = highlightedText;
        }
      },
  },
  mounted() {
    this.fetchResult();
  }
}
</script>
  
  