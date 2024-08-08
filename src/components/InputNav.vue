<script lang="ts" setup>
import { ref, inject } from 'vue'
import { io } from 'socket.io-client';
const room: any = inject("room");
const socket = io('http://localhost:5000');
const newOrder: any = inject('newOrder')
const voteFlag: any = inject('voteFlag')
const addOrder = () => {
    if (!newOrder.value.shop_name) {
        alert('請輸入店家名稱');
        return;
    }
    else {
        voteFlag.value = true;
        socket.emit('new-order', {
            room: room.value,
            shop_info: newOrder.value
        });
    }
}

</script>
<template>
    <div class="nav">

        <div class="info2">
            <label>店家名稱&nbsp;<i class="bi bi-shop"></i></label>
            <input v-model="newOrder.shop_name" class="send-input" type="text"></input>
        </div>
        <br />
        <div class="info2">
            <label>備註&nbsp;<i class="bi bi-stickies"></i></label>
            <input v-model="newOrder.remark" class="send-input" type="text"></input>
        </div>
        <br />
        <button class="add-shop-btn" @click="addOrder"><i class="bi bi-plus-lg"></i></button>
    </div>
</template>
<style scoped>
.nav {
    position: relative;
    font-size: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    width: 310px;
    height: fit-content;
    border-right: 1px solid #333333;
}

.info2 {
    display: flex;
    width: 300px;
    justify-content: space-between;
    font-size: 20px;
    padding-top: 10px;
    text-align: center;

}

.send-input {
    border: none;
    background-color: transparent;
    border-bottom: #333333 solid 1px;
    font-size: 15px;
}

.send-input:focus {
    outline: none;
    border-bottom: #5f40e7 solid 3px;

}

.add-shop-btn {
    height: 30px;
    color: #f8f8f8;
    background: #5f40e7;
    border: none;
    font-size: 20px;
}

.add-shop-btn:hover {
    color: #5f40e7;
    background: #f8f8f8;
    cursor: pointer;
}
</style>