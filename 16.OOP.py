class Hewan:
    def __init__(hewan, jenis):
        hewan.jenis = jenis

class Anjing(Hewan):
    def __init__(anjing, name, gender):
        super().__init__("Anjing")
        anjing.name = name
        anjing.gender = gender
        
class Kucing(Hewan):
    def __init__(kucing, name, gender):
        super().__init__("Kucing")
        kucing.name = name
        kucing.gender = gender

martha = Anjing("martha", "Cewe")
rico = Kucing("Rico", "Laki")

print(f"""
      jenis : {martha.jenis}
      nama  : {martha.name}
      gender: {martha.gender}
      """)

print(f"""
      jenis : {rico.jenis}
      nama  : {rico.name}
      gender: {rico.gender}
      """)