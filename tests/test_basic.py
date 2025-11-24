#!/usr/bin/env python 3
"""
Basic test file for E xpense Tracker
This file tests the basic functi onality and structure

"""

import sys
import os

#   Add the src directory to Pyth on path
sys.path.append  (os.path.join(os.path.dirname (__file__), '.. /src'))



def test_imports() :
    """Test if all required modules can be im ported"""  


    try :

        import json

        import os

        from datetime import datetime

        print( "All standard imports work" )

        return True
    
    except ImportError as e :

        print(f" Import error: {e}")

        return False

def test_file_structure() :

    """Test if project files exist"""

    required_files =   [
        'src/expense_tracker.py' ,

        'README.md' ,

        'statement.md' ,


        'requirements.txt'
    ]

    
    all_exist = True

    for file in required_files :


        if os.path.exists(file ) :


            print(f" {file} exists")


        else :


            print(f" {file} missing")


            all_exist = False
    
    return all_exist

def test_data_file_creation  () :


    """Test if data file can be created"""
    try :

        ## Test JSON operations


        test_data = [ {"amount":  100.0 , "category" : "Test" , "description" : "Test expense" }]

        with open('test_data.json', 'w') as f : 


            import json

            json.dump(test_data, f )

        
        ### Read it   ba ck

        with open('test_data.json', 'r') as f :

            loaded_data =  json.load(f )


        
        ####   Clean up


        os.remove ('test_data.json')

        
        if loaded_data[0]['amount'] == 100.0 :

            print(" Data file operations work")

            return True
        

        else :

            print(" Data file test failed")

            return False
            
    except Exception as e:
        print(f" Data file test error: {e}")
        return False

def run_all_tests()  :


    """Run all basic   t ests"""


    print( " Running Basic Tests..."  )


    print("=" * 50)


    
    tests = [
        test_imports , 


        test_file_structure ,


        test_data_file_creation
    ]
    
    passed = 0

    total = len(tests)

    
    for test in tests :

        if test():


            passed += 1


    
    print("=" * 50)


    print(f"Test Results: {passed}/{total} tests passed")
    
    
    if passed == total : 


        print( " All basic tests passed! Your project structure is correct." )

    else:

        print(" Some tests failed. Please check your project structure.")
    
    return passed == total

if __name__ == "__main__" :


    run_all_tests()