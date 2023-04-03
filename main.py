from save_json import writeAJson
from database import Database
from crud import LivroModel

db = Database(database="biblioteca", collection="livros")
db.resetDatabase()
data = db.collection.find()

livros = LivroModel(db)

livro_id = livros.criar_livro("Diario de um banana", "Jeff Kinney")

book1 = livros.ler_livro(livro_id)

livros.atualizar_livro(2, "Mobie Dick", "Herman Melville")

livros.deletar_livro(livro_id)