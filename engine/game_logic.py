from .philosophy import get_philosophical_quote

def run_game(story):
    karma = 0
    for scene in story["scenes"]:
        print(f"\n{scene['text']}")
        for idx, choice in enumerate(scene['choices'], 1):
            print(f"{idx}. {choice['text']}")

        print("\n" + get_philosophical_quote('good' if karma >= 0 else 'bad'))
        
        while True:
            try:
                selection = int(input("Pilih tindakanmu: "))
                if 1 <= selection <= len(scene['choices']):
                    break
            except ValueError:
                pass
            print("Masukkan angka yang valid.")

        chosen = scene['choices'][selection - 1]
        print(f"\n{chosen['consequence']}")
        karma += chosen.get("karma", 0)

    return karma
