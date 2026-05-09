class WebSocketClient {
  private socket: WebSocket = new WebSocket("ws://localhost:8000/ws")
  private listeners = new Map<string, ((data: any) => void)>()

  constructor() {
    this.socket.onmessage = (e) => {
      const msg = JSON.parse(e.data)
      this.listeners.get(msg.id)!(msg.data)
    }
  }

  onMessage(id: string, callback: (data: any) => void) {
    this.listeners.set(id,callback)
  }

  sendMessage(id: string, data: any) {
    this.socket.send(JSON.stringify({ id: id, data: data }))
  }
}

export const ws = new WebSocketClient()

