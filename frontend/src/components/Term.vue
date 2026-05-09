<template>
  <div ref="terminalRef" class="xterm-container"></div>
</template>

<script setup lang="ts">
import {ws} from './WebSocketManger';
import { ref, onMounted } from 'vue'
import { Terminal } from 'xterm'
import {fromByteArray, toByteArray } from "base64-js";
import 'xterm/css/xterm.css'

const terminalRef = ref<HTMLElement>()
let term = new Terminal()

onMounted(() => {
  term.open(terminalRef.value!)

  term.onData((data: string) => {
    const data_bytes = fromByteArray(new TextEncoder().encode(data))
    ws.sendMessage('1',data_bytes)
  })
})

ws.onMessage(
  '1',
  (data)=>{
  term.write(toByteArray(data))
})

</script>

<style scoped>
.xterm-container {
  width: 100%;
}
</style>