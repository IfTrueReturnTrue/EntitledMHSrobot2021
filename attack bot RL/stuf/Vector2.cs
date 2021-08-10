using System;

namespace stuf
{

    public class Vector2
    {
        public double x_component;
        public double y_component;



        public Vector2(double radius, double theta)
        {
            x_component = radius * Math.Cos(theta);
            x_component = radius * Math.Sin(theta);
        }
    }
}
