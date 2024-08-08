<script lang="ts" setup>
import shopCard from "./shopCard.vue"
import { ref, inject } from 'vue'
const shop_info: any = inject('orders')
</script>
<template>
    <div class="line">
    </div>
        <shopCard v-for="(info, index) in shop_info" :key="index" :shop_name="info.shop_name" :remark="info.remark" :oppo="info.oppo"/>
    
</template>
<style scoped>
.line{
    position: absolute;
    top:-2.5px;
    display: flex;
    border-top: 10px solid rgb(72, 46, 2); /* 變更箭頭的高度和顏色 */
    z-index: 30;
    width: 100vw ;
}
</style>