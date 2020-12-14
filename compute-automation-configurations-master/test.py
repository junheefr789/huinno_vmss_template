from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = "Endpoint=sb://ty-huinno-sb-space.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=mQDdM20ZqAZCSTRsXj3Lh/WLakxiaQUR6shvPTY03F0="
QUEUE_NAME = "huinno_analysis"
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    while True:
        try:
            receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=5,session_id='testSession')
            
            with receiver:
                for msg in receiver:
                    print("Received: " + str(msg))
                    receiver.complete_message(msg)
        except:
            print('에러발생')
            continue