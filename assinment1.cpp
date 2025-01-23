#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

const double RADIUS = 6371.0;

double degreesToRadians(double degrees) {
    return degrees * M_PI / 180.0;
}

double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
    double latDiff = degreesToRadians(lat2 - lat1);
    double lonDiff = degreesToRadians(lon2 - lon1);

    lat1 = degreesToRadians(lat1);
    lat2 = degreesToRadians(lat2);

    double a = std::sin(latDiff / 2) * std::sin(latDiff / 2) +
               std::cos(lat1) * std::cos(lat2) *
               std::sin(lonDiff / 2) * std::sin(lonDiff / 2);
    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));

    return RADIUS * c;
}

int main() {
    std::vector<std::pair<double, double>> list1 = {
        {37.7749, -122.4194},
        {34.0522, -118.2437}
    };

    std::vector<std::pair<double, double>> list2 = {
        {40.7128, -74.0060},
        {41.8781, -87.6298},
        {29.7604, -95.3698}
    };

    for (const auto& point1 : list1) {
        double closestDist = std::numeric_limits<double>::max();
        std::pair<double, double> closestPoint;

        for (const auto& point2 : list2) {
            double dist = calculateDistance(point1.first, point1.second, point2.first, point2.second);
            if (dist < closestDist) {
                closestDist = dist;
                closestPoint = point2;
            }
        }

        std::cout << "Closest to (" << point1.first << ", " << point1.second << ") is ("
                  << closestPoint.first << ", " << closestPoint.second << ") with "
                  << closestDist << " km.\n";
    }

    return 0;
}
