from fastapi import FastAPI, status, Depends, HTTPException

from src.models.aluno import AlunoModel
from src.schemas.aluno import AlunoSchema

from db.database import get_session
from src.api.routers.routers import api_router

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

# Exemplos apenas para teste

app = FastAPI()
app.include_router(api_router)

@app.get('/', status_code=status.HTTP_200_OK)
def teste():
    return {"teste": "teste"}

@app.post('/aluno', status_code=status.HTTP_201_CREATED, response_model=AlunoSchema)
async def post_aluno(aluno: AlunoSchema, db: AsyncSession = Depends(get_session)):
    aluno_novo = AlunoModel(**aluno.dict())

    db.add(aluno_novo)
    await db.commit()
    print('deu bom')

    return aluno_novo
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)