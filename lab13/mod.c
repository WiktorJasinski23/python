#include <Python.h>
#include "funkcje.h"

static PyObject *mod_met2(PyObject *self, PyObject *args){
	PyObject *list;
	if(!PyArg_ParseTuple(args, "O", &list)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
    int* arr = NULL;

	int r= (int)PyList_Size(list);
	arr = (int *) malloc(sizeof(int *) * r);
	for(int i=0; i<r; i++){
        PyObject *el;
	    el = PyList_GetItem(list, i);
        arr[i] = (int) PyLong_AsLong(el);
	}

    Py_BuildValue("i", bubble_sort(r));
    PyObject* pyList = PyList_New(r);
    for (int i = 0; i < r; ++i){
        PyObject* python_int = Py_BuildValue("i", arr[i]);
        PyList_SetItem(pyList, i, python_int);
    }


	return pyList;
}

static PyObject *mod_met(PyObject *self, PyObject *args){
	int a,b,c;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
    int* arr = NULL;

   	if(d){
		int r= (int)PyList_Size(d);
		arr = (int *) malloc(sizeof(int *) * r);
		for(int i=0; i<r; i++){
		    PyObject *el;
			el = PyList_GetItem(d, i);
            arr[i] = (int) PyLong_AsLong(el);
		}
		for(int i=0; i<r; i++){
			s += arr[i];
		}

	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
	{"met2", (PyCFunction)mod_met2, METH_VARARGS, "Funkcja ..."},
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
