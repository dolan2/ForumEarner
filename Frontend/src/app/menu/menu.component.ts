import {Component, Input, OnInit} from '@angular/core';
import {Post} from '../models/post.interface';
import {Bar} from '../models/bar.class';
import {Pie} from '../models/pie.class';
import {Linear, Series} from '../models/linear.class';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  @Input() posts: Post[];
  dataStack: Bar[];
  dataSalary: Bar[];
  dataExperience: Bar[];
  dataLocation: Bar[];

  dataAge: Pie[];
  dataContractType: Pie[];

  dataSalaryToExperienceByStack: Linear[];
  dataSalaryToExperienceByLocation: Linear[];
  dataSalaryToAgeByStack: Linear[];
  dataSalaryToAgeByLocation: Linear[];

  ngOnInit(): void {
    this.chartAge();
    this.charContractType();

    this.chartLocation();
    this.chartExperience();
    this.chartStack();
    this.chartSalary();

    this.chartSalaryToExperienceByStack();
    this.chartSalaryToExperienceByLocation();
    this.chartSalaryToAgeByStack();
    this.chartSalaryToAgeByLocation();
  }

  chartSalaryToExperienceByStack() {
    this.dataSalaryToExperienceByStack = [];
    const uniqueStack = new Set(this.posts.map(post => post.stack));

    uniqueStack.forEach(stack => {
      this.dataSalaryToExperienceByStack.push(new Linear(stack));
    });

    this.posts.forEach(post => {
      this.dataSalaryToExperienceByStack
        .find(x => x.name === post.stack).series
        .push(new Series(Math.round(post.exp).toString(), post.salary));
    });

    this.dataSalaryToExperienceByStack.forEach(data => {
      const seriesMap = new Map();
      data.series.forEach(series => {
        if (seriesMap.has(series.name)) {
          seriesMap.set(series.name, seriesMap.get(series.name) + series.value);
        } else {
          seriesMap.set(series.name, series.value);
        }
      });

      const tempArray = [];
      seriesMap.forEach((value, key) => {
        tempArray.push(new Series(key, value));
      });

      data.series = tempArray;
    });

    this.dataSalaryToExperienceByStack.forEach(data => {
      data.series.forEach(series => {
        series.value = Math.round(series.value / this.posts.filter(x => x.stack === data.name)
          .filter(y => Math.round(y.exp) === +series.name).length);
      });
    });

    this.dataSalaryToExperienceByStack.map(data => {
      data.series.sort((m, n) => (+m.name > +n.name) ? 1 : -1);
    });
  }

  chartSalaryToExperienceByLocation() {
    this.dataSalaryToExperienceByLocation = [
      new Linear('Other'),
      new Linear('Śląsk'),
      new Linear('Trójmiasto')
    ];

    const uniqueLocation = new Set(this.posts.map(post => post.location));

    uniqueLocation.forEach(location => {
      if (location.indexOf('Trójmiasto') < 0 && location.indexOf('Śląsk') < 0 && location.indexOf('Other') < 0) {
        this.dataSalaryToExperienceByLocation.push(new Linear(location));
      }
    });

    this.posts.forEach(post => {
      this.dataSalaryToExperienceByLocation
        .find(x => post.location.includes(x.name)).series
        .push(new Series(Math.round(post.exp).toString(), post.salary));
    });

    this.dataSalaryToExperienceByLocation.forEach(data => {
      const seriesMap = new Map();
      data.series.forEach(series => {
        if (seriesMap.has(series.name)) {
          seriesMap.set(series.name, seriesMap.get(series.name) + series.value);
        } else {
          seriesMap.set(series.name, series.value);
        }
      });

      const tempArray = [];
      seriesMap.forEach((value, key) => {
        tempArray.push(new Series(key, value));
      });

      data.series = tempArray;
    });

    this.dataSalaryToExperienceByLocation.forEach(data => {
      data.series.forEach(series => {
        series.value = Math.round(series.value / this.posts.filter(x => x.location.includes(data.name))
          .filter(y => Math.round(y.exp) === +series.name).length);
      });
    });

    this.dataSalaryToExperienceByLocation.map(data => {
      data.series.sort((m, n) => (+m.name > +n.name) ? 1 : -1);
    });

  }

  chartSalaryToAgeByStack() {
    this.dataSalaryToAgeByStack = [];
    const uniqueStack = new Set(this.posts.map(post => post.stack));

    uniqueStack.forEach(stack => {
      this.dataSalaryToAgeByStack.push(new Linear(stack));
    });

    this.posts.forEach(post => {
      this.dataSalaryToAgeByStack
        .find(x => x.name === post.stack).series
        .push(new Series(Math.round(post.age).toString(), post.salary));
    });

    this.dataSalaryToAgeByStack.forEach(data => {
      const seriesMap = new Map();
      data.series.forEach(series => {
        if (seriesMap.has(series.name)) {
          seriesMap.set(series.name, seriesMap.get(series.name) + series.value);
        } else {
          seriesMap.set(series.name, series.value);
        }
      });

      const tempArray = [];
      seriesMap.forEach((value, key) => {
        tempArray.push(new Series(key, value));
      });

      data.series = tempArray;
    });

    this.dataSalaryToAgeByStack.forEach(data => {
      data.series.forEach(series => {
        series.value = Math.round(series.value / this.posts.filter(x => x.stack === data.name)
          .filter(y => Math.round(y.age) === +series.name).length);
      });
    });

    this.dataSalaryToAgeByStack.map(data => {
      data.series.sort((m, n) => (+m.name > +n.name) ? 1 : -1);
    });
  }

  chartSalaryToAgeByLocation() {

    // const rangeAge = [
    //   new Linear('Younger than 15 years'),
    //   new Linear('15 to 19 years'),
    //   new Linear('20 to 24 years'),
    //   new Linear('25 to 29 years'),
    //   new Linear('30 to 34 years'),
    //   new Linear('35 to 39 years'),
    //   new Linear('40 to 44 years'),
    //   new Linear('45 to 49 years'),
    //   new Linear('50 to 54 years'),
    //   new Linear('55 to 59 years'),
    //   new Linear('60 years and older')
    // ];

    this.dataSalaryToAgeByLocation = [
      new Linear('Other'),
      new Linear('Śląsk'),
      new Linear('Trójmiasto')
    ];

    const uniqueLocation = new Set(this.posts.map(post => post.location));

    uniqueLocation.forEach(location => {
      if (location.indexOf('Trójmiasto') < 0 && location.indexOf('Śląsk') < 0 && location.indexOf('Other') < 0) {
        this.dataSalaryToAgeByLocation.push(new Linear(location));
      }
    });

    this.posts.forEach(post => {
      this.dataSalaryToAgeByLocation
        .find(x => post.location.includes(x.name)).series
        .push(new Series(Math.round(post.age).toString(), post.salary));
    });

    this.dataSalaryToAgeByLocation.forEach(data => {
      const seriesMap = new Map();
      data.series.forEach(series => {
        if (seriesMap.has(series.name)) {
          seriesMap.set(series.name, seriesMap.get(series.name) + series.value);
        } else {
          seriesMap.set(series.name, series.value);
        }
      });

      const tempArray = [];
      seriesMap.forEach((value, key) => {
        tempArray.push(new Series(key, value));
      });

      data.series = tempArray;
    });

    this.dataSalaryToAgeByLocation.forEach(data => {
      data.series.forEach(series => {
        series.value = Math.round(series.value / this.posts.filter(x => x.location.includes(data.name))
          .filter(y => Math.round(y.age) === +series.name).length);
      });
    });

    this.dataSalaryToAgeByLocation.map(data => {
      data.series.sort((m, n) => (+m.name > +n.name) ? 1 : -1);
    });
  }

  chartAge() {
    this.dataAge = [
      new Bar('Younger than 15 years', 0),
      new Bar('15 to 19 years', 0),
      new Bar('20 to 24 years', 0),
      new Bar('25 to 29 years', 0),
      new Bar('30 to 34 years', 0),
      new Bar('35 to 39 years', 0),
      new Bar('40 to 44 years', 0),
      new Bar('45 to 49 years', 0),
      new Bar('50 to 54 years', 0),
      new Bar('55 to 59 years', 0),
      new Bar('60 years and older', 0)
    ];

    this.posts.forEach(post => {
      if (post.age < 15) {
        this.dataAge.filter(x => x.name === 'Younger than 15 years').map(y => y.value += 1);
      } else if (post.age >= 15 && post.age < 20) {
        this.dataAge.filter(x => x.name === '15 to 19 years').map(y => y.value += 1);
      } else if (post.age >= 20 && post.age < 25) {
        this.dataAge.filter(x => x.name === '20 to 24 years').map(y => y.value += 1);
      } else if (post.age >= 25 && post.age < 30) {
        this.dataAge.filter(x => x.name === '25 to 29 years').map(y => y.value += 1);
      } else if (post.age >= 30 && post.age < 35) {
        this.dataAge.filter(x => x.name === '30 to 34 years').map(y => y.value += 1);
      } else if (post.age >= 35 && post.age < 40) {
        this.dataAge.filter(x => x.name === '35 to 39 years').map(y => y.value += 1);
      } else if (post.age >= 40 && post.age < 45) {
        this.dataAge.filter(x => x.name === '40 to 44 years').map(y => y.value += 1);
      } else if (post.age >= 45 && post.age < 50) {
        this.dataAge.filter(x => x.name === '45 to 49 years').map(y => y.value += 1);
      } else if (post.age >= 50 && post.age < 55) {
        this.dataAge.filter(x => x.name === '50 to 54 years').map(y => y.value += 1);
      } else if (post.age >= 55 && post.age < 60) {
        this.dataAge.filter(x => x.name === '55 to 59 years').map(y => y.value += 1);
      } else if (post.age >= 60) {
        this.dataAge.filter(x => x.name === '60 years and older').map(y => y.value += 1);
      }
    });
  }

  chartStack() {
    this.dataStack = [];
    const uniqueStack = new Set(this.posts.map(post => post.stack));

    uniqueStack.forEach(stack => {
      this.dataStack.push(new Bar(stack, 0));
    });

    this.posts.forEach(post => {
      this.dataStack.filter(x => x.name === post.stack).map(y => y.value += 1);
    });
    this.dataStack.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

  chartExperience() {
    this.dataExperience = [];
    const uniqueStack = new Set(this.posts.map(post => Math.round(+post.exp)));

    uniqueStack.forEach(contractType => {
      this.dataExperience.push(new Bar(contractType.toString(), 0));
    });

    this.posts.forEach(post => {
      this.dataExperience.filter(x => x.name === Math.round(+post.exp).toString()).map(y => y.value += 1);
    });
    this.dataExperience.sort((m, n) => (+m.name > +n.name) ? 1 : -1);
  }

  chartSalary() {
    this.dataSalary = [
      new Bar('Less than 3000 pln', 0),
      new Bar('3000 to 3999 pln', 0),
      new Bar('4000 to 4999 pln', 0),
      new Bar('5000 to 5999 pln', 0),
      new Bar('6000 to 6999 pln', 0),
      new Bar('7000 to 7999 pln', 0),
      new Bar('8000 to 8999 pln', 0),
      new Bar('9000 to 9999 pln', 0),
      new Bar('10000 to 10999 pln', 0),
      new Bar('11000 to 11999 pln', 0),
      new Bar('12000 to 12999 pln', 0),
      new Bar('13000 to 13999 pln', 0),
      new Bar('14000 to 14999 pln', 0),
      new Bar('15000 to 15999 pln', 0),
      new Bar('16000 to 16999 pln', 0),
      new Bar('17000 to 17999 pln', 0),
      new Bar('18000 to 18999 pln', 0),
      new Bar('19000 to 19999 pln', 0),
      new Bar('20000 to 20999 pln', 0),
      new Bar('21000 to 21999 pln', 0),
      new Bar('22000 to 22999 pln', 0),
      new Bar('23000 to 23999 pln', 0),
      new Bar('24000 to 24999 pln', 0),
      new Bar('More than 25000 pln', 0),
    ];

    this.posts.forEach(post => {
      if (post.salary >= 2000 && post.salary < 3000) {
        this.dataSalary.filter(x => x.name === 'Less than 3000 pln').map(y => y.value += 1);
      } else if (post.salary >= 3000 && post.salary < 4000) {
        this.dataSalary.filter(x => x.name === '3000 to 3999 pln').map(y => y.value += 1);
      } else if (post.salary >= 4000 && post.salary < 5000) {
        this.dataSalary.filter(x => x.name === '4000 to 4999 pln').map(y => y.value += 1);
      } else if (post.salary >= 5000 && post.salary < 6000) {
        this.dataSalary.filter(x => x.name === '5000 to 5999 pln').map(y => y.value += 1);
      } else if (post.salary >= 6000 && post.salary < 7000) {
        this.dataSalary.filter(x => x.name === '6000 to 6999 pln').map(y => y.value += 1);
      } else if (post.salary >= 7000 && post.salary < 8000) {
        this.dataSalary.filter(x => x.name === '7000 to 7999 pln').map(y => y.value += 1);
      } else if (post.salary >= 8000 && post.salary < 9000) {
        this.dataSalary.filter(x => x.name === '8000 to 8999 pln').map(y => y.value += 1);
      } else if (post.salary >= 9000 && post.salary < 10000) {
        this.dataSalary.filter(x => x.name === '9000 to 9999 pln').map(y => y.value += 1);
      } else if (post.salary >= 10000 && post.salary < 11000) {
        this.dataSalary.filter(x => x.name === '10000 to 10999 pln').map(y => y.value += 1);
      } else if (post.salary >= 11000 && post.salary < 12000) {
        this.dataSalary.filter(x => x.name === '11000 to 11999 pln').map(y => y.value += 1);
      } else if (post.salary >= 12000 && post.salary < 13000) {
        this.dataSalary.filter(x => x.name === '12000 to 12999 pln').map(y => y.value += 1);
      } else if (post.salary >= 13000 && post.salary < 14000) {
        this.dataSalary.filter(x => x.name === '13000 to 13999 pln').map(y => y.value += 1);
      } else if (post.salary >= 14000 && post.salary < 15000) {
        this.dataSalary.filter(x => x.name === '14000 to 14999 pln').map(y => y.value += 1);
      } else if (post.salary >= 15000 && post.salary < 16000) {
        this.dataSalary.filter(x => x.name === '15000 to 15999 pln').map(y => y.value += 1);
      } else if (post.salary >= 16000 && post.salary < 17000) {
        this.dataSalary.filter(x => x.name === '16000 to 16999 pln').map(y => y.value += 1);
      } else if (post.salary >= 17000 && post.salary < 18000) {
        this.dataSalary.filter(x => x.name === '17000 to 17999 pln').map(y => y.value += 1);
      } else if (post.salary >= 18000 && post.salary < 19000) {
        this.dataSalary.filter(x => x.name === '18000 to 18999 pln').map(y => y.value += 1);
      } else if (post.salary >= 19000 && post.salary < 20000) {
        this.dataSalary.filter(x => x.name === '19000 to 19999 pln').map(y => y.value += 1);
      } else if (post.salary >= 20000 && post.salary < 21000) {
        this.dataSalary.filter(x => x.name === '20000 to 20999 pln').map(y => y.value += 1);
      } else if (post.salary >= 21000 && post.salary < 22000) {
        this.dataSalary.filter(x => x.name === '21000 to 21999 pln').map(y => y.value += 1);
      } else if (post.salary >= 22000 && post.salary < 23000) {
        this.dataSalary.filter(x => x.name === '22000 to 2999 pln').map(y => y.value += 1);
      } else if (post.salary >= 23000 && post.salary < 24000) {
        this.dataSalary.filter(x => x.name === '23000 to 23999 pln').map(y => y.value += 1);
      } else if (post.salary >= 24000 && post.salary < 25000) {
        this.dataSalary.filter(x => x.name === '24000 to 24999 pln').map(y => y.value += 1);
      } else if (post.salary >= 25000) {
        this.dataSalary.filter(x => x.name === 'More than 25000 pln').map(y => y.value += 1);
      }
    });
  }

  charContractType() {
    this.dataContractType = [];
    const uniqueStack = new Set(this.posts.map(post => post.contract_type));

    uniqueStack.forEach(contractType => {
      this.dataContractType.push(new Bar(contractType, 0));
    });

    this.posts.forEach(post => {
      this.dataContractType.filter(x => x.name === post.contract_type).map(y => y.value += 1);
    });
    this.dataContractType.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

  chartLocation() {
    this.dataLocation = [
      new Bar('Other', 0),
      new Bar('Śląsk', 0),
      new Bar('Trójmiasto', 0)
    ];

    const uniqueStack = new Set(this.posts.map(post => post.location));

    uniqueStack.forEach(location => {
      if (location.indexOf('Trójmiasto') < 0 && location.indexOf('Śląsk') < 0 && location.indexOf('Other') < 0) {
        this.dataLocation.push(new Bar(location, 0));
      }
    });

    this.posts.forEach(post => {
      if (post.location.indexOf('Trójmiasto') >= 0) {
        this.dataLocation.filter(x => x.name === 'Trójmiasto').map(y => y.value += 1);
      } else if (post.location.indexOf('Śląsk') >= 0) {
        this.dataLocation.filter(x => x.name === 'Śląsk').map(y => y.value += 1);
      } else if (post.location.indexOf('Other') >= 0) {
        this.dataLocation.filter(x => x.name === 'Other').map(y => y.value += 1);
      } else {
        this.dataLocation.filter(x => x.name === post.location).map(y => y.value += 1);
      }
    });
    this.dataLocation.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

}
