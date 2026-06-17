from nostr_sdk import Keys, NostrSigner, Client, EventBuilder, RelayUrl, HandleNotification, PublicKey, Filter
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
    keys = Keys.generate()
    secret_key_str = "suachave"
    public_key_str = "npub1g60puz8mme77f738xm0y25tc6ukjtlfxjz0h4y3379rm6ktpvasq2ucs6u"
    
    pri_key = secret_key_str
    pub_key = public_key_str

    print(f"Public Key: {pub_key}")
    print(f"Private Key: {pri_key}")

    #signer = NostrSigner.keys(keys)
    signer = NostrSigner.keys(Keys.parse(pri_key))
    client = Client(signer)
    

    relay_url = RelayUrl.parse("wss://relay.damus.io")
    await client.add_relay(relay_url)
    await client.connect()


    builder = EventBuilder.text_note("Hello, Nostr!")
    try:
        output = await client.send_event_builder(builder)
        print(f"Evento enviado com sucesso! ID: {output.id.to_hex()}")
    except Exception as e:
        print(f"Erro ao enviar evento: {e}")



    pubkey = PublicKey.parse(pub_key)
    filter = Filter().author(pubkey).limit(5)
    
    print("Conectado ao relay. Aguardando eventos...")
    await client.subscribe(filter)
    await client.handle_notifications(NotificationHandler())
if __name__ == "__main__":
    asyncio.run(main())
