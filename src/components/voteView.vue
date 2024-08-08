<script lang="ts" setup>
import { ref, computed, provide, inject } from 'vue';
const voteFlag: any = inject('voteFlag')
const orders: any = inject('orders')
const newOrder: any = inject('newOrder')
const finished: any = inject('finished');
const userNum : any = inject('userNum');
const people = ref(new Array(userNum.value.length).fill(''));
const hasVoted = ref(false);
const clickOk = ref(true);
const clickNo = ref(true);

const voteOkCount = ref(0);
const voteNoCount = ref(people.value.length - 1);
const voteCount = ref(0);
const vote = (isAgree: boolean) => {
    if (voteCount.value < people.value.length) {


        if (voteOkCount.value > voteNoCount.value) {
            return;
        }
        if (isAgree) {
            people.value[voteOkCount.value] = '#a4e2cf'; // 同意顏色
            voteOkCount.value++;
            clickNo.value = false;
            if (voteOkCount.value == people.value.length) {
                finished.value = true;
            }
        } else {
            people.value[voteNoCount.value] = '#e2aba4'; // 不同意顏色
            voteNoCount.value--;
            clickOk.value = false;
            // 這裡接後端
            newOrder.value.oppo += (localStorage.getItem('username')) + " ";
        }
        hasVoted.value = true;
        voteCount.value++;
        if (voteCount.value >= people.value.length)
            // 這裡接後端
            setTimeout(() => {
                voteFlag.value = false;
                orders.value.push({ ...newOrder.value })
                newOrder.value = {
                    shop_name: '',
                    remark: '',
                    oppo: ""
                }
            }, 2000);
    }
};

const processedRemark = computed(() => {
    let remarkWithPrefix = `備註&nbsp;${newOrder.value.remark}`;

    // 然后将URL替换为超链接
    return remarkWithPrefix.replace(/(\bhttps?:\/\/[^\s/$.?#].[^\s]*)/gi, '<a href="$1" target="_blank">$1</a>');

});

</script>
<template>
    <div class="vote-bg">
        <div class="vote-con">
            <h1 class="h1-note">注意!!!</h1>
            <!-- 店家 -->
            <h2 :title="newOrder.shop_name" class="remark2 vote-shop">店名&nbsp;{{ newOrder.shop_name }}</h2>
            <!-- 備註 -->
            <h5 class="remark2 vote-shop" v-html="processedRemark"></h5>
            <div class="votes">
                <i v-for="(person, index) in people" :key="index" class="bi bi-person-fill"
                    :style="{ color: person }"></i>
            </div>
            <button class="vote-ok" @click="vote(true)" :disabled="hasVoted" v-if="clickOk">Yes</button>
            <button class="vote-no" @click="vote(false)" :disabled="hasVoted" v-if="clickNo">No</button>
        </div>
    </div>
</template>
<style>
.remark2 {
    display: -webkit-box;
    -webkit-line-clamp: 6;
    -webkit-box-orient: vertical;
    overflow: hidden;
    word-break: break-all;
}

.votes {
    display: flex;
    width: 100%;
    position: absolute;
    justify-content: center;
    bottom: 30%;
}

.bi-person-fill {
    font-size: 2rem;
    color: #777777;
}

.vote-shop {
    padding-left: 150px;
    padding-right: 150px;
}

.h1-note {
    position: relative;
    left: 45%;
}

.vote-ok {
    position: absolute;
    width: 20%;
    height: 80px;
    bottom: 80px;
    left: 30%;
    background-color: #a4e2cf;
    border: 1px solid #fafffd;
    cursor: pointer;
    color: #fafffd;
    font-size: 20px;
}

.vote-no {
    color: #fafffd;
    font-size: 20px;
    cursor: pointer;
    position: absolute;
    width: 20%;
    height: 80px;
    bottom: 80px;
    left: 50%;
    background-color: #e2aba4;
    border: 1px solid #fafffd;
}

.vote-con {
    position: absolute;
    width: 60%;
    height: 70%;
    top: 15%;
    left: 20%;
    background-color: #ffffffe4;
    border: none;
    border-radius: 15px;

}

.vote-bg {
    position: absolute;
    width: 100vw;
    height: 100vh;
    background-color: rgba(144, 144, 144, 0.416);
    z-index: 30;
}
</style>