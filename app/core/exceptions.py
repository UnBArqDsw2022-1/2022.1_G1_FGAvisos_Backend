from fastapi import HTTPException, status


class Exceptions:
    @staticmethod
    def default_exception(erro: str = "Erro"):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exeção -> {erro}"
        )

    @staticmethod
    def nao_encontrado(objeto: str):
        return HTTPException(
            detail=f'{objeto} não encontrado',
            status_code=status.HTTP_404_NOT_FOUND
        )

    @staticmethod
    def nao_encontrados(objeto: str):
        return HTTPException(
            detail=f'Nenhum(a) {objeto} foi encontrado(a)',
            status_code=status.HTTP_404_NOT_FOUND
        )

    @staticmethod
    def bad_request(erro: str = "Erro"):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=erro
        )

    @staticmethod
    def nao_autorizado(finalidade: str = "realizar esta acao"):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Você não possui autorização para {finalidade}"
        )

    @staticmethod
    def credenciais_invalida():
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não foi possível validar as credenciais."
        )

    @staticmethod
    def sem_altorizacao(finalidade: str = "realizar esta acao"):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Você não possui autorização para {finalidade}"
        )

    @staticmethod
    def acesso_incorreto():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Dados de acesso incorretos.'
        )