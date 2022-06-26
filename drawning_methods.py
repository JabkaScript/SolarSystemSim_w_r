import os.path

from solar_system_stat import *
import window_init
import math_base
import sys

def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return path

def draw_focus(object):
    if not window_init.SCALED:
        set_planet_scale()

        math_base.clear_scaled_orbits(object)
        window_init.SCALED = True
    object.draw(window_init.WIN)


def draw_satellites(focus_object):
    for i in range(abs(math_base.timestep_tick)):
        math_base.calculate_next_position_for_satellites(focus_object)
    focus_object.draw_satellites(window_init.WIN)


def define_main_objects_images():
    Sun.image = pygame.image.load(resource_path("planets/sun.png"))
    Mercury.image = pygame.image.load(resource_path("planets/mercury.png"))
    Venus.image = pygame.image.load(resource_path("planets/venus.png"))
    Earth.image = pygame.image.load(resource_path("planets/earth.png"))
    Mars.image = pygame.image.load(resource_path("planets/mars.png"))
    Jupiter.image = pygame.image.load(resource_path("planets/jupiter.png"))
    Saturn.image = pygame.image.load(resource_path("planets/saturn.png"))
    Uranus.image = pygame.image.load(resource_path("planets/uranus.png"))
    Neptune.image = pygame.image.load(resource_path("planets/neptune.png"))

    Moon.image = pygame.image.load(resource_path("satellites/moon.png"))

    Phobos.image = pygame.image.load(resource_path("satellites/phobos.png"))
    Deimos.image = pygame.image.load(resource_path("satellites/deimos.png"))

    Io.image = pygame.image.load(resource_path("satellites/io.png"))
    Europe.image = pygame.image.load(resource_path("satellites/europe.png"))

    Titan.image = pygame.image.load(resource_path("satellites/titan.png"))
    Enceladus.image = pygame.image.load(resource_path("satellites/enceladus.png"))

    Titania.image = pygame.image.load(resource_path("satellites/titania.png"))
    Oberon.image = pygame.image.load(resource_path("satellites/oberon.png"))

    Triton.image = pygame.image.load(resource_path("satellites/triton.png"))




def set_planet_scale():
    Sun.drawable_image = pygame.transform.scale(Sun.image, (Sun.radius // math_base.planet_scale,
                                                            Sun.radius // math_base.planet_scale))
    Mercury.drawable_image = pygame.transform.scale(Mercury.image, (Mercury.radius // math_base.planet_scale,
                                                                    Mercury.radius // math_base.planet_scale))
    Venus.drawable_image = pygame.transform.scale(Venus.image, (Venus.radius // math_base.planet_scale,
                                                                Venus.radius // math_base.planet_scale))
    Earth.drawable_image = pygame.transform.scale(Earth.image, (Earth.radius // math_base.planet_scale,
                                                                Earth.radius // math_base.planet_scale))
    Mars.drawable_image = pygame.transform.scale(Mars.image, (Mars.radius // math_base.planet_scale,
                                                              Mars.radius // math_base.planet_scale))
    Jupiter.drawable_image = pygame.transform.scale(Jupiter.image, (Jupiter.radius // math_base.planet_scale,
                                                                    Jupiter.radius // math_base.planet_scale))
    Saturn.drawable_image = pygame.transform.scale(Saturn.image, (Saturn.radius // math_base.planet_scale,
                                                                  Saturn.radius // math_base.planet_scale))
    Uranus.drawable_image = pygame.transform.scale(Uranus.image, (Uranus.radius // math_base.planet_scale,
                                                                  Uranus.radius // math_base.planet_scale))
    Neptune.drawable_image = pygame.transform.scale(Neptune.image, (Neptune.radius // math_base.planet_scale,
                                                                    Neptune.radius // math_base.planet_scale))
    Moon.drawable_image = pygame.transform.scale(Moon.image, (Moon.radius // math_base.planet_scale,
                                                              Moon.radius // math_base.planet_scale))
    Phobos.drawable_image = pygame.transform.scale(Phobos.image, (Phobos.radius // math_base.planet_scale,
                                                                  Phobos.radius // math_base.planet_scale))
    Deimos.drawable_image = pygame.transform.scale(Deimos.image, (Deimos.radius // math_base.planet_scale,
                                                                  Deimos.radius // math_base.planet_scale))
    Io.drawable_image = pygame.transform.scale(Io.image, (Io.radius // math_base.planet_scale,
                                                              Io.radius // math_base.planet_scale))
    Europe.drawable_image = pygame.transform.scale(Europe.image, (Europe.radius // math_base.planet_scale,
                                                          Europe.radius // math_base.planet_scale))
    Titan.drawable_image = pygame.transform.scale(Titan.image, (Titan.radius // math_base.planet_scale,
                                                                  Titan.radius // math_base.planet_scale))
    Enceladus.drawable_image = pygame.transform.scale(Enceladus.image, (Enceladus.radius // math_base.planet_scale,
                                                                Enceladus.radius // math_base.planet_scale))
    Titania.drawable_image = pygame.transform.scale(Titania.image, (Titania.radius // math_base.planet_scale,
                                                                Titania.radius // math_base.planet_scale))
    Oberon.drawable_image = pygame.transform.scale(Oberon.image, (Oberon.radius // math_base.planet_scale,
                                                                    Oberon.radius // math_base.planet_scale))
    Triton.drawable_image = pygame.transform.scale(Triton.image, (Triton.radius // math_base.planet_scale,
                                                                  Triton.radius // math_base.planet_scale))


def draw_UI(UI):
    UI.draw_background()
    UI.draw_buttons()

