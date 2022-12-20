import OpenGL

from OpenGL.GL import *


from OpenGL.GLUT import *

from OpenGL.GLU import *

from datetime import datetime






i=0.0
j=0.0
k=0.0

def initGL():
	global i
	global j
	global k
	glClearColor(0.0,0.1,0.0,0.1)
	now=datetime.now()
	sec=int(now.strftime("%S"))
	min=int(now.strftime("%M"))
	hr=int(now.strftime("%H"))
	i=-6*sec
	j=-6*min
	k=-30*hr



def disp(id=0):
	global i
	global j
	global k
	glClear(GL_COLOR_BUFFER_BIT)
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glColor3f(0.0,1.0,1.0)

	glVertex2f(0.0,0.7)
	glVertex2f(0.0,0.6)

	glVertex2f(0.38,0.7)
	glVertex2f(0.34,0.6)

	glVertex2f(-0.38,0.7)
	glVertex2f(-0.34,0.6)


	glVertex2f(-0.38,-0.7)
	glVertex2f(-0.34,-0.6)


	glVertex2f(0.7,0.35) 
	glVertex2f(0.6,0.32)

	glVertex2f(0.7,-0.35) 
	glVertex2f(0.6,-0.32)



	glVertex2f(-0.7,-0.35) 
	glVertex2f(-0.6,-0.32)




	glVertex2f(-0.7,0.35) 
	glVertex2f(-0.6,0.32)


	glVertex2f(-0.7,0.35) 
	glVertex2f(-0.6,0.32)



	glVertex2f(0.7,0.0) 
	glVertex2f(0.6,0.0)


	glVertex2f(0.0,-0.7) 
	glVertex2f(0.0,-0.6)


	glVertex2f(0.38,-0.7) 
	glVertex2f(0.34,-0.6)



	glVertex2f(-0.7,0.0) 
	glVertex2f(-0.6,0.0)

	glEnd()



	glLoadIdentity()
	glBegin(GL_LINES)
	glColor3f(1.0,1.0,1.0)
	

	glVertex2f(0.7,0.7)
	glVertex2f(-0.7,0.7)

	glVertex2f(-0.7,0.7)
	glVertex2f(-0.7,-0.7)

	glVertex2f(-0.7,-0.7)
	glVertex2f(0.7,-0.7)

	glVertex2f(0.7,-0.7)
	glVertex2f(0.7,0.7)

	glVertex2f(0.75,0.75)
	glVertex2f(-0.75,0.75)

	glVertex2f(-0.75,0.75)
	glVertex2f(-0.75,-0.75)

	glVertex2f(-0.75,-0.75)
	glVertex2f(0.75,-0.75)

	glVertex2f(0.75,-0.75)
	glVertex2f(0.75,0.75)


	glEnd()




	glPushMatrix()
	glRotatef(i,0.0,0.0,0.1)
	glLineWidth(2.0)
	glBegin(GL_LINES)
	glColor3f(0.0,1.0,0.0)#second
	glVertex2f(0.0,0.0)
	glVertex2f(0.0,0.6)


	glEnd()
	glPopMatrix()



	glPushMatrix()
	glRotatef(j,0.0,0.0,0.1)
	glLineWidth(3.0)
	glBegin(GL_LINES)
	glColor3f(1.0,1.0,1.0)#min
	glVertex2f(0.0,0.0)
	glVertex2f(0.0,0.5)

	glEnd()
	glPopMatrix()


	glPushMatrix()
	glRotatef(k,0.0,0.0,0.1)
	glLineWidth(6.0)
	glBegin(GL_LINES)
	glColor3f(1.0,1.0,0.0)#hour
	glVertex2f(0.0,0.0)
	glVertex2f(0.0,0.3)

	glEnd()
	glPopMatrix()

	i-=6
	if i<=-360:
		if j<=360:
			k-=5.0
			i=0.0
			j=0.0
		else:
			j-=6.0
			i=0.0

	glutTimerFunc(1000,disp,0)
	glutSwapBuffers()


def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
	glutInitWindowSize(600, 600)
	glutCreateWindow("CLOCK")
	initGL()
	glutDisplayFunc(disp)
	glutMainLoop()

main()

