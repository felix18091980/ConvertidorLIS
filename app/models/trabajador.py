"""
Modelo de datos de un trabajador.
"""

from dataclasses import dataclass, field


@dataclass
class Trabajador:
    codigo: str = ""
    dni: str = ""
    nombre: str = ""
    cargo: str = ""

    banco: str = ""
    cuenta: str = ""

    afp: str = ""
    cuspp: str = ""

    haberes: dict = field(default_factory=dict)
    descuentos: dict = field(default_factory=dict)

    total_haberes: float = 0.0
    total_descuentos: float = 0.0
    liquido: float = 0.0

    def agregar_haber(self, concepto, importe):
        self.haberes[concepto] = importe

    def agregar_descuento(self, concepto, importe):
        self.descuentos[concepto] = importe

    def __str__(self):
        return (
            f"{self.codigo} - {self.nombre} "
            f"(Haberes: {self.total_haberes:.2f}, "
            f"Descuentos: {self.total_descuentos:.2f}, "
            f"Líquido: {self.liquido:.2f})"
        )
