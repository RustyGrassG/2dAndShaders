from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *

#render a single point
class Test(Base):

    def initialize(self):
        print("Initializing program")

        ##Initialize program##

        #vertex shader code
        vsCode = """
        void main()
        {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """

        #fragment shader code
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        #Send code to the GPU and compile; storethe program reference
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ###set up vertex array object###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ###Render Settings###

        #Set point width and heigh
        glPointSize(10)

    def update(self):

        #Select program to use when rendering
        glUseProgram(self.programRef)

        #Renders the geomentric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)

Test().run()