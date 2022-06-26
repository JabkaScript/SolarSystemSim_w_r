from space_objects import *
import math_base
import solar_system_object_information_ru
import os, sys


def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return path

Sun = SpaceObject("Солнце", 0, 0, "yellow", 1.98892 * 10 ** 30, 69599000, "Звезда")
Sun.info = solar_system_object_information_ru.sun_info
Sun.real_image = resource_path("planets/sun_R.jpg")

Mercury = SpaceObject("Меркурий", 0.38709830982 * math_base.AU, 0, "yellow", 3.30 * 10 ** 23, 2439000, "Планета")
Mercury.y_velocity = 47.87 * 1000
Mercury.info = solar_system_object_information_ru.mercury_info
Mercury.real_image = resource_path("planets/mercury_R.jpg")

Venus = SpaceObject("Венера", 0.72332981996 * math_base.AU, 0, "orange", 4.87 * 10 ** 24, 6052000, "Планета")
Venus.y_velocity = 35.02 * 1000
Venus.info = solar_system_object_information_ru.venus_info
Venus.real_image = resource_path("planets/venus_R.jpg")


Earth = SpaceObject("Земля", 1.00000101778*math_base.AU, 0, "green", 5.97 * 10 ** 24, 6371000, "Планета")
Earth.y_velocity = 29.79 * 1000
Earth.info = solar_system_object_information_ru.earth_info
Earth.real_image = resource_path("planets/earth_R.jpg")

Mars = SpaceObject("Марс", 1.52367934191 * math_base.AU, 0, "red", 6.42 * 10 ** 24, 3389000, "Планета")
Mars.y_velocity = 24.13 * 1000
Mars.info = solar_system_object_information_ru.mars_info
Mars.real_image = resource_path("planets/mars_R.jpg")

Jupiter = SpaceObject("Юпитер", 5.20260319132 * math_base.AU, 0, (180, 134, 128), 1.8986 * 10 ** 27, 34911000, "Планета")
Jupiter.y_velocity = 13.06 * 1000
Jupiter.info = solar_system_object_information_ru.jupiter_info
Jupiter.real_image = resource_path("planets/jupiter_R.jpg")

Saturn = SpaceObject("Сатурн", 9.54 * math_base.AU, 0, (230, 212, 176), 5.68 * 10 ** 26, 58232000, "Планета")
Saturn.y_velocity = 9.66 * 1000
Saturn.info = solar_system_object_information_ru.saturn_info
Saturn.real_image = resource_path("planets/saturn_R.jpg")

Uranus = SpaceObject("Уран", 19.2 * math_base.AU, 0, (191, 255, 255), 8.68 * 10 ** 25, 25362000, "Планета")
Uranus.y_velocity = 6.80 * 1000
Uranus.info = solar_system_object_information_ru.uranus_info
Uranus.real_image = resource_path("planets/uranus_R.jpg")

Neptune = SpaceObject("Нептун", 30.1*math_base.AU, 0, (75, 112, 221), 1.02*10**26, 24662000, "Планета")
Neptune.y_velocity = 5.4349*1000
Neptune.info = solar_system_object_information_ru.neptune_info
Neptune.real_image = resource_path("planets/neptune_R.jpg")

Moon = SpaceObject("Луна", 384467*1000, 0, "gray", 7.35 * 10 ** 22, 1737000, "Спутник")
Moon.y_velocity = 1.02*1000
Moon.original_y_velocity = 1.02*1000
Moon.real_image = resource_path("satellites/moon_R.jpg")
Moon.info = solar_system_object_information_ru.moon_info
Earth.satellite_array.append(Moon)

Phobos = SpaceObject("Фобос", 93800*1000, 0, "gray", 1.072 * 10 ** 16, 1340000, "Спутник")
Phobos.y_velocity = 2.14*1000
Phobos.original_y_velocity = 2.14*1000
Phobos.real_image = resource_path("satellites/phobos_R.jpg")
Phobos.info = solar_system_object_information_ru.phobos_info
Mars.satellite_array.append(Phobos)

Deimos = SpaceObject("Деймос", 234600*1000, 0, "red", 1.48 * 10 ** 15, 620000, "Спутник")
Deimos.y_velocity = 1.35*1000
Deimos.original_y_velocity = 1.35*1000
Deimos.real_image = resource_path("satellites/deimos_R.jpg")
Deimos.info = solar_system_object_information_ru.deimos_info
Mars.satellite_array.append(Deimos)

Io = SpaceObject("Ио", 421800*1000, 0, "yellow", 8.94*10**22, 3660000, "Спутник")
Io.y_velocity = 17.334*1000
Io.original_y_velocity = 17.334*1000
Io.real_image = resource_path("satellites/io_R.jpg")
Io.info = solar_system_object_information_ru.io_info
Jupiter.satellite_array.append(Io)

Europe = SpaceObject("Европа", 671100*1000, 0, "white", 4.8*10**22, 3138000, "Спутник")
Europe.y_velocity = 13.74*1000
Europe.original_y_velocity = 13.74*1000
Europe.real_image = resource_path("satellites/europe_R.jpg")
Europe.info = solar_system_object_information_ru.europe_info
Jupiter.satellite_array.append(Europe)

Enceladus = SpaceObject("Энцелад", 237378*1000, 0, "gray", 1.08022*10**20, 252000, "Спутник")
Enceladus.y_velocity = 12.51*1000
Enceladus.original_y_velocity = 12.51*1000
Enceladus.real_image = resource_path("satellites/enceladus_R.jpg")
Enceladus.info = solar_system_object_information_ru.titan_info
Saturn.satellite_array.append(Enceladus)

Titan = SpaceObject("Титан", 1221000*1000, 0, "yellow", 1350*10**20, 2575000, "Спутник")
Titan.y_velocity = 5.57*1000
Titan.original_y_velocity = 5.57*1000
Titan.real_image = resource_path("satellites/titan_R.jpg")
Titan.info = solar_system_object_information_ru.titan_info
Saturn.satellite_array.append(Titan)

Titania = SpaceObject("Титания", 436298*1000, 0, "white", 3.527*10**21, 1608000, "Спутник")
Titania.y_velocity = 3.64*1000
Titania.original_y_velocity = 3.64*1000
Titania.real_image = resource_path("satellites/titania_R.jpg")
Titania.info = solar_system_object_information_ru.titania_info
Uranus.satellite_array.append(Titania)

Oberon = SpaceObject("Оберон", 583519*1000, 0, "gray", 3.014*10**21, 1408000, "Спутник")
Oberon.y_velocity = 3.15*1000
Oberon.original_y_velocity = 3.15*1000
Oberon.real_image = resource_path("satellites/oberon_R.jpg")
Oberon.info = solar_system_object_information_ru.oberon_info
Uranus.satellite_array.append(Oberon)

Triton = SpaceObject("Тритон", 354759*1000, 0, "gray", 2.14*10**22, 1353000, "Спутник")
Triton.y_velocity = -4.38*1000
Triton.original_y_velocity = -4.38*1000
Triton.real_image = resource_path("satellites/triton_R.jpg")
Triton.info = solar_system_object_information_ru.triton_info
Neptune.satellite_array.append(Triton)

Sun.satellite_array = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
OBJECT_ARRAY = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
