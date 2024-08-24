<script lang="ts" setup>
import gameMain from "../gameMain.vue"
import inputnav from "../InputNav.vue"
import voteView from "../voteView.vue"
import { ref, provide, watch, onMounted, nextTick, onUnmounted } from "vue"
import { io } from 'socket.io-client';
import { useRoute } from 'vue-router';
const route = useRoute();
const room = ref(route.params.room);
const user: string|null = localStorage.getItem('username');
const users = ref([]);
let ws : WebSocket ;
const updateRoomUsers = (roomUsers: any) => {
    users.value = roomUsers.length;
};
function joinRoom(name:String, roomId:String) {
    ws = new WebSocket(`ws://140.128.101.24:8080/${roomId}`);

    ws.onopen = function () {
        console.log("Connected to the WebSocket server.");
        ws.send(JSON.stringify({ type: "join", name: name }));
    };

    ws.onclose = function () {
        console.log("Disconnected from the WebSocket server.");
    };

    ws.onerror = function (error) {
        console.error("WebSocket error: ", error);
    };
}
onMounted(() => {
    if (user && room.value) {
        return joinRoom(user as string, room.value as string);
    }
});
onUnmounted(() => {
});
const finished = ref(false);
const shop_info = ref([])
// const shop_info = ref([
//     {
//         shop_name: "shop1",
//         remark: "site1",
//         oppo: ""
//     },
//     {
//         shop_name: "shop2",
//         remark: "site2",
//         oppo: ""
//     },
//     {
//         shop_name: "shop3",
//         remark: "site3",
//         oppo: ""
//     }

// ])
const newOrder = ref({
    shop_name: '',
    remark: '',
    oppo: ""
})
const voteFlag = ref(false);
provide("ws",ws)
provide("room", room)
provide("voteFlag", voteFlag)
provide("newOrder", newOrder)
provide('orders', shop_info)
provide("finished", finished)
provide("userNum", users)
const gameView: any = ref(null);
watch(shop_info, () => {
    nextTick(() => {
        gameView.value.scrollLeft = gameView.value.scrollWidth;
        gameView.value.width = gameView.value.scrollWidth;

    });
}, { deep: true });
</script>
<template>
    <div class="room-container" ref="gameView">
        <div class="game-view">
            <gameMain></gameMain>
        </div>
        <div class="foot">
            <i class="bi bi-paperclip clip-icon"></i>
            <inputnav></inputnav>
        </div>
        <div class="foot2">
        </div>
        <voteView v-if="voteFlag"></voteView>
        <!-- 補放結束畫面 -->
    </div>
</template>
<style scoped>
.clip-icon {
    position: relative;
    font-size: 45px;
    left: 5px;
    top: -30px;
    color: #0d202c;
}

.room-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow-x: scroll;
}

.game-view {
    position: relative;
    width: 100vw;
    height: 60%;
    border: none;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    top: 100px;
}

.foot {
    width: 310px;
    height: 300px;
    background: linear-gradient(to bottom, #fefefe, #e3e3e3);
    border: 3px solid #626262;
    box-shadow: 3px 3px 1px 3px rgba(0, 0, 0, 0.2);
    position: fixed;
    bottom: 40px;
    left: 70%;
    z-index: 1;
}

.foot2 {
    width: 310px;
    height: 300px;
    background: linear-gradient(to bottom, #fefefe, #e3e3e3);
    border: 3px solid #626262;
    box-shadow: 3px 3px 1px 3px rgba(0, 0, 0, 0.2);
    position: fixed;
    bottom: 35px;
    left: 70.3%;
}
</style>