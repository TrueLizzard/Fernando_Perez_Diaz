import argparse
from pathlib import Path
import sys

def renombrar_logs(directorio: Path, nombre: str, apellido: str) -> int:
    if not directorio.exists() or not directorio.is_dir():
        raise FileNotFoundError(f"Directorio no válido: {directorio}")
    
    logs = sorted([p for p in directorio.iterdir() if p.is_file() and p.suffix.lower() == ".log"],
                  key=lambda p: p.name.lower())
    
    count = 0
    for i, p in enumerate(logs, start=1):
        nuevo = directorio / f"{nombre.lower()}_{apellido.lower()}_{i}.log"
        
        if nuevo.exists():
            nuevo = directorio / f"{nombre.lower()}_{apellido.lower()}_{i}__dup.log"
        
        p.rename(nuevo)
        count += 1
    
    return count

def main():
    parser = argparse.ArgumentParser(description="Renombra archivos .log a nombre_apellido_<n>.log")
    parser.add_argument("directorio", type=Path, help="Ruta del directorio con los .log")
    parser.add_argument("--nombre", required=True, help="Nombre para el nuevo archivo")
    parser.add_argument("--apellido", required=True, help="Apellido para el nuevo archivo")
    args = parser.parse_args()
    n = renombrar_logs(args.directorio, args.nombre, args.apellido)
    print(f"Renombrados: {n}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)