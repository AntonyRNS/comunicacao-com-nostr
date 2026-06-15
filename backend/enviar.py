from nostr_sdk import Keys, NostrSigner, Client, EventBuilder, SecretKey, RelayUrl
import asyncio

async def main():
    keys = Keys.generate()
    SecretKey = "nsec1ek35as9jq0gfjhdm2ep47pzr3829mnhz7y3vdscgqul5nstq057q0t8qkp"
    PublicKey = "npub1g60puz8mme77f738xm0y25tc6ukjtlfxjz0h4y3379rm6ktpvasq2ucs6u"
    
    # pub_key = keys.public_key().to_hex()
    # pri_key = keys.secret_key().to_hex()
    pri_key = SecretKey
    pub_key = PublicKey
    

    print(f"Public Key: {pub_key}")
    print(f"Private Key: {pri_key}")

    #signer = NostrSigner.keys(keys)
    signer = NostrSigner.keys(Keys.parse(pri_key))
    client = Client(signer)
    

    relay_url = RelayUrl.parse("wss://relay.damus.io")
    await client.add_relay(relay_url)
    await client.connect()


    builder = EventBuilder.text_note("Teste definitivo, Nostr!")
    try:
        output = await client.send_event_builder(builder)
        print(f"Evento enviado com sucesso! ID: {output.id.to_hex()}")
    except Exception as e:
        print(f"Erro ao enviar evento: {e}")
    finally:
        await client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
