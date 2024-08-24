<script setup lang="ts">
import { ref, watch, onBeforeMount, onMounted } from "vue";
import axios from 'axios';
import { useRouter } from "vue-router";
import { type UserInter } from "@/types";
const router = useRouter();
const inputOkFlag = ref(false);
const user = ref<UserInter>({
    name: "",
    room: "",
});
onBeforeMount(() => {
    const preName: string | null = localStorage.getItem('username');
    if (preName != null) {
        user.value.name = preName;
    }
})
watch(user, () => {
    if (user.value.name != "" && user.value.room != "") {
        inputOkFlag.value = true;
    }
    else {
        inputOkFlag.value = false;
    }
}, { deep: true })
// import { io } from 'socket.io-client';
// const socket = io('http://localhost:5000');
// function sendData() {
//     if (user.value.name != "" && user.value.room != "") {
//         localStorage.setItem('username', user.value.name);
//         localStorage.setItem('room', user.value.room);
//         router.push({ name: 'Room', params: { room: String(user.value.room) } })
//     }
//     else{
//         alert("請輸入暱稱或房號")
//     }
// }
const myButton = ref<HTMLButtonElement | null>(null);
onMounted(() => {
    document.addEventListener('keydown', handleKeyDown);
});

function handleKeyDown(event: KeyboardEvent) {
    if (event.key === 'Enter' && inputOkFlag.value) {
        myButton.value?.click();
    }
}
const createRoomAndJoin = async () => {
  try {
    const response = await axios.post('http://140.128.101.24:8080/get_room_id');
    const roomId = response.data;
    localStorage.setItem('username', user.value.name);
    localStorage.setItem('room', roomId);
    router.push({ name: 'Room', params: { room: String(roomId) } })
    
  } catch (error) {
    console.error('Error creating room:', error);
  }
};
const joinRoom = async () => {
    localStorage.setItem('username', user.value.name);
    localStorage.setItem('room', user.value.room);
    router.push({ name: 'Room', params: { room: String(user.value.room) } })
}
</script>

<template>
    <div class="login-bg">
        <div class="container">
            <h1>登入</h1>
            <div class="login-info">
                <div class="info">
                    <label>暱稱&nbsp;<i class="bi bi-pencil"></i>
                    </label>
                    <input class="login-input" type="text" placeholder="請輸入暱稱" v-model="user.name">
                </div>
                <div class="info">
                    <label>加入房間&nbsp;<i class="bi bi-123"></i></label>
                    <input class="login-input" type="number" placeholder="請輸入房號" v-model="user.room">
                </div>
                <hr />
                or
                <hr />
                <button class="create-room-btn" @click="createRoomAndJoin">創建房間</button>
            </div>
            <button ref="myButton" v-if="inputOkFlag" class="login-btn" @click="joinRoom"><i
                    class="bi bi-arrow-right"></i></button>
        </div>
    </div>
</template>
<style scoped>
.create-room-btn {
    border: none;
    border-radius: 10px;
    background: #E0E0E0;
    color: #333333;
    font-size: 18px;
    width: 84px;
    height: 50px;
    background: linear-gradient(to left, #E0E0E0 50%, #333333 50%) right;
    background-size: 300%;
    transition: .5s ease-out;
}

.create-room-btn:hover {
    background-position: left;
    color: #efefef;
    cursor: pointer;
}

.login-input {
    border: none;
    background-color: transparent;
    border-bottom: #333333 solid 1px;

}

.login-input:focus {
    outline: none;
    border-bottom: #5f40e7 solid 3px;

}

.login-btn {
    position: absolute;
    width: 50px;
    height: 50px;
    border-radius: 15px;
    color: #333333;
    background: #efefef;
    background: linear-gradient(to left, #efefef 50%, #333333 50%) right;
    background-size: 300%;
    transition: .5s ease-out;
    border: none;
    font-size: 20px;
    bottom: 76px;
    right: 100px;
}

.login-btn:hover {
    background-position: left;
    color: #efefef;
    cursor: pointer;
}

h1 {
    position: relative;
    font-size: 50px;
    top: 100px;

}



.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

}

.login-bg {
    position: absolute;
    width: 500px;
    height: 600px;
    border-radius: 25px;
    border: none;
    top: 50%;
    left: 50%;
    margin: -300px 0 0 -250px;
    background-color: #E0E0E0;
    box-shadow: 0 0 20px 10px rgba(51, 51, 51, 0.25);
}

.login-info {
    position: relative;
    top: 150px;
    font-size: large;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>