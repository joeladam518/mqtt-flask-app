export default {
    keepalive: 60, //  seconds, set to 0 to disable
    clientId: 'vue_mqtt_' + Math.random().toString(16).substr(2, 8),
    protocolId: 'MQTT',
    //username: '',
    //password: '',
    incomingStore: {},
    outgoingStore: {},
}