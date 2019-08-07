import rospy
from std_msgs.msg import String, Int32
# from geometry_msgs.msg import Point
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse

class Node(object):

    def __init__(self):
        rospy.init_node('simple_node', log_level=rospy.DEBUG)
        self.__init_params()
        self.__init_pub()
        self.__init_sub()
        self.__init_srv()

    def __init_params(self):
        self.param1 = rospy.get_param('~param1', default=1.0)

    def __init_pub(self):
        self.msg_pub = rospy.Publisher('msg', String, queue_size=0)

    def __init_sub(self):
        self.num_sub = rospy.Subscriber('num', Int32, callback=self._num_callback, queue_size=1)

    def __init_srv(self):
        self.toggle_srv = rospy.Service('toggle', SetBool, self._toggle_callback)

    def _num_callback(self, msg):
        # msg es de tipo std_msgs.msg.Int32
        rospy.loginfo(str(msg))
        return

    def _toggle_callback(self, request):
        # request es de tipo std_srvs.srv.SetBoolRequest
        rospy.loginfo(str(request.data))
        response = SetBoolResponse(True, 'response')
        return response

    def _pub_msg(self, msg):
        # msg debe ser de tipo std_msgs.msg.String
        self.msg_pub.publish(msg)

    def algun_metodo(self):
        x = "Hola"
        y = "Mundo"
        self._pub_msg("%s %s" % (x, y))

    def run(self):
        # Si el nodo no debe hacer ninguna tarea (porque se maneja solo con callbacks)
        # rospy.spin()

        rospy.loginfo('Starting node')

        rate = rospy.Rate(1.0)

        while not rospy.is_shutdown():
            # Hacer cosas

            self.algun_metodo()
            rate.sleep()
