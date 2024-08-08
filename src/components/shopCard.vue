<script lang="ts" setup>
import { computed, inject } from 'vue';
const voteFlag: any = inject('voteFlag');
const newOrder: any = inject('newOrder');

const props = defineProps({
    shop_name: String,
    remark: String,
    oppo: String,
});
function rollback() {
    newOrder.value.shop_name = props.shop_name;
    newOrder.value.remark = props.remark;
    newOrder.value.oppo = "";
    voteFlag.value = true;
}
const isOppo = computed(() => {
    const usernmae: any = localStorage.getItem('username');
    if (props.oppo) {
        return props.oppo.split(" ").includes(usernmae)
    }
    return false;
});
const processedRemark = computed(() => {
    let remarkWithPrefix = `備註&nbsp;${props.remark}`;

    // 然后将URL替换为超链接
    return remarkWithPrefix.replace(/(\bhttps?:\/\/[^\s/$.?#].[^\s]*)/gi, '<a href="$1" target="_blank">$1</a>');

});
</script>
<template>
    <div class="shop-card">
        <i class="bi bi-paperclip clip-icon2"></i>
        <i v-if="isOppo" class="bi bi-arrow-clockwise rotating-icon" style="font-size: 50px;" @click="rollback"></i>
        <h2 :title="shop_name" class="remark">店名&nbsp;{{ shop_name }}</h2>
        <h4 :title="oppo" class="remark">{{ oppo }}反對</h4>
        <h5 class="remark" :title="remark" v-html="processedRemark"></h5>
    </div>
</template>
<style scoped>
.remark {
    display: -webkit-box;
    -webkit-line-clamp: 6;
    -webkit-box-orient: vertical;
    overflow: hidden;
    word-break: break-all;
}

.clip-icon2 {
    font-size: 50px;
    position: absolute;
    top: -30px;
    color: #0d202c;
    padding-top: 250px;
    margin-top: -250px;
}

.rotating-icon {
    position: absolute;
    left: -25px;
    top: 50px;
    animation: transform-icon 5s infinite linear;
    display: inline-block;
    color: rgb(147, 3, 3);
    cursor: pointer;
}

@keyframes transform-icon {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(359deg);
    }
}

.shop-card {
    position: relative;
    flex: 0 0 auto;
    left: 50px;
    margin-left: 50px;
    margin-right: 10%;
    padding: 10px;
    padding-left: 30px;
    width: 260px;
    height: 240px;
    background: linear-gradient(to bottom, #fefefe, #e3e3e3);
    border: 3px solid #626262;
    box-shadow: 3px 3px 1px 3px rgba(0, 0, 0, 0.2);
}

.shop-card::before {
    content: '';
    position: absolute;
    top: -5px;
    /* 將頂部邊框上移 30px */
    left: -150px;
    /* 左側延伸距離 */
    width: calc(100% + 260px);
    /* 讓邊框比容器寬度長 */
    height: 10px;
    /* 邊框高度 */
    background-color: rgb(72, 46, 2);
    z-index: 1;
    /* 確保在內容上面 */
}

.shop-card::after {
    content: '';
    width: 0;
    height: 0;
    border-top: 30px solid black;
    /* 變更箭頭的高度和顏色 */
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-left: 10px solid rgb(167, 163, 172);
    /* 箭頭顏色 */
    position: absolute;
    right: -20px;
    /* 調整箭頭位置 */
    top: 50%;
    transform: translateY(-50%);
}
</style>