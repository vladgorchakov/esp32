        def get_temp(self):
            try:
                self.__ds.convert_temp()
                time.sleep(1)
                self.temp = self.__ds.read_temp(self.__roms[0])
                return self.__temp
            except OneWireError:
                print(f'Проверьте правильность подключения датчика!')
                
                



