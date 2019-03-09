// 使用template标签来定义html部分
<template>
<div class="breadcrumb" @click="fnLight">
  当前位置：<span :class="{hot:isHot}">{{pos}}</span>
</div>
</template>

// javascript要写成模块导出的形式：
<script>
export default{
  props: ['pos'],
  name: 'crump',
  data: function () {
    return {
      isHot: false
    }
  },
  methods: {
    fnLight: function () {
      this.isHot = !this.isHot
    }
  }
}
</script>

// 样式中如果有scope关键字，表示这些样式是组件局部的，不会影响其他元素
<style scoped>
.breadcrumb{
    width:90%;
    line-height:50px;
    border-bottom:1px solid #ddd;
    margin:0px auto;
}
.breadcrumb .hot{
    font-weight:bold;
    color:red;
    letter-spacing:2px;
}
</style>
