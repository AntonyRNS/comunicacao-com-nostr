from nostr_sdk import Client, Filter, RelayUrl, PublicKey, HandleNotification
import asyncio

class NotificationHandler(HandleNotification):
    async def handle(self, relay_url, subscription_id, event):
        if event.kind().as_u16() == 1:  
            print(f"\nNOVO EVENTO!")
            print(f"ID: {event.id().to_hex()}")
            print(f"Autor (Hex): {event.author().to_hex()}")
            print(f"Conteúdo: {event.content()}")
            print(f"Timestamp: {event.created_at().as_secs()}")

    async def handle_msg(self, relay_url, msg):
        pass

async def main():
    client = Client()
    
    relay_url = RelayUrl.parse("wss://relay.damus.io")
    await client.add_relay(relay_url)
    await client.connect()
    
   
    pubkey = PublicKey.parse("npub1g60puz8mme77f738xm0y25tc6ukjtlfxjz0h4y3379rm6ktpvasq2ucs6u")
    filter = Filter().author(pubkey).limit(5)
    
    print("Conectado ao relay. Aguardando eventos...")
    
    await client.subscribe(filter)

    await client.handle_notifications(NotificationHandler())


if __name__ == "__main__":
    asyncio.run(main())