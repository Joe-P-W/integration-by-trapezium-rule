def integrate(equation, between: list = [0, 1],
              accuracy: float = 0.0001) -> float:
    """
    equation = Function Object or Lambda expression
    between = List (Optional will default to [0, 1])
    accuracy = float (Optional will default to 0.0001)

    equation - arguement is the equation of the line you wish to
    integrate and example input for an x^2 line would be: lambda x: x**2

    between - arguement is which to posisions on the graph you wish to
    inegrate between for exmple between = [5, 10] will integrate between
    5 and 10.

    accuracy - arguement that determines the hight of you trapeziums
    the smaller this number the smaller error there will be between the
    actual answer and the answer returned.
    """

    def trapz_area(top, bottom, height): return ((top+bottom)/2)*height
    top = between[0]
    bottom = between[0] + accuracy
    height = accuracy
    area = 0

    while bottom <= between[1]:
        area += trapz_area(equation(top), equation(bottom), height)
        top += accuracy
        bottom += accuracy

    return area
