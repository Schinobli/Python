class Conversao:
    @staticmethod
    def binario(ip: int) -> str:
        binarios = [128, 64, 32, 16, 8, 4, 2, 1]
        aux = ''
        for n in binarios:
            if n > ip:
                aux += '0'
            else:
                aux += '1'
                ip -= n
        return aux

    @staticmethod
    def mascara_rede(masc):
        host = ('1' * masc) + ('0' * (32 - masc))
        return host

    @staticmethod
    def nro_ip(masc: int):
        return 2 ** (32 - masc) - 2

    @staticmethod
    def decimal(bin_ip: str):
        count = 0
        binarios = [128, 64, 32, 16, 8, 4, 2, 1,
                    128, 64, 32, 16, 8, 4, 2, 1,
                    128, 64, 32, 16, 8, 4, 2, 1,
                    128, 64, 32, 16, 8, 4, 2, 1]
        aux = ''
        for index, valor in enumerate(bin_ip):
            if index in [8, 16, 24]:
                aux += str(count) + '.'
                count = 0
            if valor == '1':
                count += binarios[index]
            if index == 31:
                aux += str(count)

        return aux

    @staticmethod
    def calcula_rede(ip_rede, mascara):
        list_ip = ip_rede.split('.')
        ip_bin = ''
        for i in list_ip:
            ip_bin += Conversao.binario(int(i))

        # IP
        print(f'IP: {ip_rede}/{mascara}')
        # Mascara rede
        print(f'Mascara da Rede: {Conversao.decimal(Conversao.mascara_rede(26))}')
        # Rede
        print(f'Rede: {Conversao.decimal(ip_bin[:mascara] + ("0" * (32 - mascara)))}/{mascara}')
        # Broadcast
        print(f'Broadcast: {Conversao.decimal(ip_bin[:mascara] + ("1" * (32 - mascara)))}/{mascara}')
        # Primeiro IP
        print(f'Primeiro IP: {Conversao.decimal(ip_bin[:mascara] + ("0" * (31 - mascara)) + "1")}/{mascara}')
        # Ultimo IP
        print(f'Ultimo IP: {Conversao.decimal(ip_bin[:mascara] + ("1" * (31 - mascara)) + "0")}/{mascara}')


Conversao.calcula_rede('10.20.12.45', 26)

