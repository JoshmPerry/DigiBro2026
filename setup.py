import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Return of Rev",
    options={"build_exe": {"packages":["pygame","time","math"],
                           "include_files":["Player/","Charger/","space_background.jpg","intro_ball.gif"]}},
    executables = executables


)
