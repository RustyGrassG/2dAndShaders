from OpenGL.GL import *

class OpenGLUtuls(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        #Specifies the required OpenGL version
        shaderCode = '#version 330\n' + shaderCode

        #Creates empty shader object
        shaderRef = glCreateShader(shaderType)
        #stores the source code into the shad4er
        glShaderSource(shaderRef, shaderCode)
        #Compiles source code previously stored in the shader object
        glCompileShader(shaderRef)

        #Checks for success
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)

        if not compileSuccess:
            #Retrieves error message
            errorMessage = glGetShaderInfoLog(shaderRef)
            #Free memory 
            glDeleteShader(shaderRef)
            #Convert Byte string to character string
            errorMessage = '\n' + errorMessage.decode('utf-8')
            #Raise exception and halt program. Print error message
            raise Exception(errorMessage)

        #Compilation was successful. Return shader
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        vertexShaderRef = OpenGLUtuls.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtuls.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        #Create empty program object and store reference to it
        programRef = glCreateProgram()

        #Attach previously compiled shader programs
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        #link vertext shader to fragment shader
        glLinkProgram(programRef)

        #chesk if link was successful
        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)
        if not linkSuccess:
            #error message
            errorMessage = glGetProgramInfoLog(programRef)
            #Free memory
            glDeleteProgram(programRef)
            #Convert to character string
            errorMessage = "\n" + errorMessage.decode('utf-8')
            #Raise Esception
            raise Exception(errorMessage)
        
        return programRef
    
    @staticmethod
    def printSystemInfo():
        print(" Vendor: " + glGetString(GL_VENDOR).decode('utf-8'))
        print("Renderer: " + glGetString(GL_RENDERER).decode('utf-8'))
        print("OpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8'))
        print(" GLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
