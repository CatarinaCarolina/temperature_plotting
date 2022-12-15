
import pytest
import temperature_plotting as tpl
import os

def test_compute_mean():
    calc = tpl.compute_mean([0,10,20])
    assert calc == 10
    assert type(calc) == float
    
    calc = tpl.compute_mean([-10,10])
    assert calc == 0
    
    calc = tpl.compute_mean([0,10,0])
    assert round(calc,4) == 3.3333, "Check digits" 
    #prints this error message if fails

    with pytest.raises(TypeError): #this is also an assertion
        calc = tpl.compute_mean(["a","b","c"])
        #if another error comes out or no error = test fails
    
    calc = tpl.compute_mean([])
    assert calc == None
    
    calc = tpl.compute_mean([1])
    assert calc == 0


def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png") 
    #files get generated when we run this! careful
    #make output dir, then delete it after the test finishes





