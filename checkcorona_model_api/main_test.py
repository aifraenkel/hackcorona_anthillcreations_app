# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    survey_inputs = {
                        "age_brackets":1,
                        "existing_disorder":0,
                        "smoking_history":0,
                        "country":"Brazil",
                        "state":"Rio de Janeiro",
                        "exposed_to_virus":0,
                        "exposed_to_risk_country":0,
                        "has_fever":0,
                        "has_related_symptoms":1
                        }

    arguments = ['age_brackets', 'country' ,'existing_disorder','exposed_to_risk_country',
                    'exposed_to_virus','has_fever','has_related_symptoms', 'smoking_history','state']


    all_feature_present = False not in [True if key in survey_inputs  else False for idx, key in enumerate(arguments) ]

    missing_arg = [arguments[idx] for idx, key in enumerate(all_feature_present) if not all_feature_present[idx]]
       
    r = client.get('/')
    assert r.status_code == 200
    assert 'Hello World' in r.data.decode('utf-8')
