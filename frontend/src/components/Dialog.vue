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
export default {
  props: {
    item: Object 
  },
  data() {
    return {
      showModal: false,
    };
  },
  methods: {
    getColorLabel(label) {
      // ラベルに対応する色を返すメソッド
      return ColorLabel[label] || 'orange'; // ラベルが定義されていない場合は 'orange'
    }
  }
};
</script>
