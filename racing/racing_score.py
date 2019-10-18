from datetime import datetime, timedelta


def _convert_to_datetime(lap):
    return datetime.strptime(lap, '%M:%S.%f').time()


def read_file(file):
    with open(file, 'r') as reader:
        next(reader)
        laps_result = reader.readline()
        driver_position_by_lap_time = {}
        driver_final_score = {}

        while laps_result:
            fields = laps_result.split()
            driver_cod = fields[1]
            driver_name = fields[3]
            lap_number = fields[4]
            lap_time = _convert_to_datetime(lap=fields[5])

            lap_time_by_driver(driver_cod, driver_name, driver_position_by_lap_time, lap_number, lap_time)

            laps_result = reader.readline()

            get_driver_result(driver_final_score, driver_position_by_lap_time)

    print('Winner', min(driver_final_score, key=driver_final_score.get))
    classification_by_time = sorted(driver_final_score.items(), key=lambda kv: kv[1])

    print(classification_by_time)


def lap_time_by_driver(driver_cod, driver_name, driver_position_by_lap_time, lap_number, lap_time):
    if driver_cod in driver_position_by_lap_time:
        driver_position_by_lap_time[driver_cod]['lap'].append(
            {
                lap_number: timedelta(
                    minutes=lap_time.minute,
                    seconds=lap_time.second,
                    microseconds=lap_time.microsecond,
                )
            }
        )
    else:
        driver_position_by_lap_time.update({
            driver_cod: {
                'driver_name': driver_name,
                'lap': [{
                    lap_number: timedelta(
                        minutes=lap_time.minute,
                        seconds=lap_time.second,
                        microseconds=lap_time.microsecond,
                    )
                }]
            }
        })


def get_driver_result(driver_final_score, driver_position_by_lap_time):
    for driver in driver_position_by_lap_time:
        if len(driver_position_by_lap_time[driver]['lap']) > 3:
            sum_of_laps = [val.total_seconds() for driver_laps in driver_position_by_lap_time[driver]['lap'] for val
                           in driver_laps.values()]
            driver_final_score.update(
                {driver + ' ' + driver_position_by_lap_time[driver]['driver_name']: sum(sum_of_laps)})


if __name__ == '__main__':
    read_file(file='../logs/racing-results.txt')
