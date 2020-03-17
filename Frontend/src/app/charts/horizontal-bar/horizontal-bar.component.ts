import {Component, Input, OnInit} from '@angular/core';
import {Post} from '../../models/post.interface';
import {HorizontalBar} from '../../models/horizontal-bar.interface';

@Component({
  selector: 'app-horizontal-bar',
  templateUrl: './horizontal-bar.component.html',
  styleUrls: ['./horizontal-bar.component.css']
})
export class HorizontalBarComponent implements OnInit {

  @Input() posts: Post[];
  data: HorizontalBar[];
  selectData: string[] = ['Age', 'Stack', 'Exp', 'Salary', 'Contract type', 'Location'];
  selected = 'Age';

  view: any[] = [1100, 600];
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = true;
  showXAxisLabel = true;
  showYAxisLabel = false;
  trimYAxisTicks = false;
  yAxisLabel = 'Age';
  xAxisLabel = 'Employees';
  colorScheme = {
    domain: ['#449dd1', '#e4572e', '#043059', '#29335C', '#669bbc', '#3b1c32', '#ca054d', '#d4e09b', '#8d5b4c', '#c4bbaf']
  };

  ngOnInit() {
    this.chartAge();
  }

  onSelectedData() {
    switch (this.selected) {
      case 'Age': {
        this.chartAge();
        break;
      }
      case 'Stack': {
        this.chartStack();
        break;
      }
      case 'Exp': {
        this.chartExp();
        break;
      }
      case 'Salary': {
        this.chartSalary();
        break;
      }
      case 'Contract type': {
        this.charContractType();
        break;
      }
      case 'Location': {
        this.chartLocation();
        break;
      }
    }
  }

  chartAge() {

    this.data = [
      new HorizontalBar('Younger than 15 years', 0),
      new HorizontalBar('15 to 19 years', 0),
      new HorizontalBar('20 to 24 years', 0),
      new HorizontalBar('25 to 29 years', 0),
      new HorizontalBar('30 to 34 years', 0),
      new HorizontalBar('35 to 39 years', 0),
      new HorizontalBar('40 to 44 years', 0),
      new HorizontalBar('45 to 49 years', 0),
      new HorizontalBar('50 to 54 years', 0),
      new HorizontalBar('55 to 59 years', 0),
      new HorizontalBar('60 years and older', 0)
    ];

    this.posts.forEach(post => {
      if (post.age < 15) {
        this.data.filter(x => x.name === 'Younger than 15 years').map(y => y.value += 1);
      } else if (post.age >= 15 && post.age < 20) {
        this.data.filter(x => x.name === '15 to 19 years').map(y => y.value += 1);
      } else if (post.age >= 20 && post.age < 25) {
        this.data.filter(x => x.name === '20 to 24 years').map(y => y.value += 1);
      } else if (post.age >= 25 && post.age < 30) {
        this.data.filter(x => x.name === '25 to 29 years').map(y => y.value += 1);
      } else if (post.age >= 30 && post.age < 35) {
        this.data.filter(x => x.name === '30 to 34 years').map(y => y.value += 1);
      } else if (post.age >= 35 && post.age < 40) {
        this.data.filter(x => x.name === '35 to 39 years').map(y => y.value += 1);
      } else if (post.age >= 40 && post.age < 45) {
        this.data.filter(x => x.name === '40 to 44 years').map(y => y.value += 1);
      } else if (post.age >= 45 && post.age < 50) {
        this.data.filter(x => x.name === '45 to 49 years').map(y => y.value += 1);
      } else if (post.age >= 50 && post.age < 55) {
        this.data.filter(x => x.name === '50 to 54 years').map(y => y.value += 1);
      } else if (post.age >= 55 && post.age < 60) {
        this.data.filter(x => x.name === '55 to 59 years').map(y => y.value += 1);
      } else if (post.age >= 60) {
        this.data.filter(x => x.name === '60 years and older').map(y => y.value += 1);
      }
    });
  }

  chartStack() {
    this.data = [];
    const uniqueStack = new Set(this.posts.map(post => post.stack));

    uniqueStack.forEach(stack => {
      this.data.push(new HorizontalBar(stack, 0));
    });

    this.posts.forEach(post => {
      this.data.filter(x => x.name === post.stack).map(y => y.value += 1);
    });
    this.data.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

  chartExp() {
    this.data = [];
    const uniqueStack = new Set(this.posts.map(post => Math.round(+post.exp)));

    uniqueStack.forEach(contractType => {
      this.data.push(new HorizontalBar(contractType.toString(), 0));
    });

    console.log(this.data);
    console.log(uniqueStack);

    this.posts.forEach(post => {
      this.data.filter(x => x.name === Math.round(+post.exp).toString()).map(y => y.value += 1);
    });
    this.data.sort((m, n) => (+m.name > +n.name) ? 1 : -1);
  }

  chartSalary() {
    this.data = [
      new HorizontalBar('Less than 3000 pln', 0),
      new HorizontalBar('3000 to 3999 pln', 0),
      new HorizontalBar('4000 to 4999 pln', 0),
      new HorizontalBar('5000 to 5999 pln', 0),
      new HorizontalBar('6000 to 6999 pln', 0),
      new HorizontalBar('7000 to 7999 pln', 0),
      new HorizontalBar('8000 to 8999 pln', 0),
      new HorizontalBar('9000 to 9999 pln', 0),
      new HorizontalBar('10000 to 10999 pln', 0),
      new HorizontalBar('11000 to 11999 pln', 0),
      new HorizontalBar('12000 to 12999 pln', 0),
      new HorizontalBar('13000 to 13999 pln', 0),
      new HorizontalBar('14000 to 14999 pln', 0),
      new HorizontalBar('15000 to 15999 pln', 0),
      new HorizontalBar('16000 to 16999 pln', 0),
      new HorizontalBar('17000 to 17999 pln', 0),
      new HorizontalBar('18000 to 18999 pln', 0),
      new HorizontalBar('19000 to 19999 pln', 0),
      new HorizontalBar('20000 to 20999 pln', 0),
      new HorizontalBar('21000 to 21999 pln', 0),
      new HorizontalBar('22000 to 22999 pln', 0),
      new HorizontalBar('23000 to 23999 pln', 0),
      new HorizontalBar('24000 to 24999 pln', 0),
      new HorizontalBar('More than 25000 pln', 0),
    ];

    this.posts.forEach(post => {
      if (post.salary >= 2000 && post.salary < 3000) {
        this.data.filter(x => x.name === 'Less than 3000 pln').map(y => y.value += 1);
      } else if (post.salary >= 3000 && post.salary < 4000) {
        this.data.filter(x => x.name === '3000 to 3999 pln').map(y => y.value += 1);
      } else if (post.salary >= 4000 && post.salary < 5000) {
        this.data.filter(x => x.name === '4000 to 4999 pln').map(y => y.value += 1);
      } else if (post.salary >= 5000 && post.salary < 6000) {
        this.data.filter(x => x.name === '5000 to 5999 pln').map(y => y.value += 1);
      } else if (post.salary >= 6000 && post.salary < 7000) {
        this.data.filter(x => x.name === '6000 to 6999 pln').map(y => y.value += 1);
      } else if (post.salary >= 7000 && post.salary < 8000) {
        this.data.filter(x => x.name === '7000 to 7999 pln').map(y => y.value += 1);
      } else if (post.salary >= 8000 && post.salary < 9000) {
        this.data.filter(x => x.name === '8000 to 8999 pln').map(y => y.value += 1);
      } else if (post.salary >= 9000 && post.salary < 10000) {
        this.data.filter(x => x.name === '9000 to 9999 pln').map(y => y.value += 1);
      } else if (post.salary >= 10000 && post.salary < 11000) {
        this.data.filter(x => x.name === '10000 to 10999 pln').map(y => y.value += 1);
      } else if (post.salary >= 11000 && post.salary < 12000) {
        this.data.filter(x => x.name === '11000 to 11999 pln').map(y => y.value += 1);
      } else if (post.salary >= 12000 && post.salary < 13000) {
        this.data.filter(x => x.name === '12000 to 12999 pln').map(y => y.value += 1);
      } else if (post.salary >= 13000 && post.salary < 14000) {
        this.data.filter(x => x.name === '13000 to 13999 pln').map(y => y.value += 1);
      } else if (post.salary >= 14000 && post.salary < 15000) {
        this.data.filter(x => x.name === '14000 to 14999 pln').map(y => y.value += 1);
      } else if (post.salary >= 15000 && post.salary < 16000) {
        this.data.filter(x => x.name === '15000 to 15999 pln').map(y => y.value += 1);
      } else if (post.salary >= 16000 && post.salary < 17000) {
        this.data.filter(x => x.name === '16000 to 16999 pln').map(y => y.value += 1);
      } else if (post.salary >= 17000 && post.salary < 18000) {
        this.data.filter(x => x.name === '17000 to 17999 pln').map(y => y.value += 1);
      } else if (post.salary >= 18000 && post.salary < 19000) {
        this.data.filter(x => x.name === '18000 to 18999 pln').map(y => y.value += 1);
      } else if (post.salary >= 19000 && post.salary < 20000) {
        this.data.filter(x => x.name === '19000 to 19999 pln').map(y => y.value += 1);
      } else if (post.salary >= 20000 && post.salary < 21000) {
        this.data.filter(x => x.name === '20000 to 20999 pln').map(y => y.value += 1);
      } else if (post.salary >= 21000 && post.salary < 22000) {
        this.data.filter(x => x.name === '21000 to 21999 pln').map(y => y.value += 1);
      } else if (post.salary >= 22000 && post.salary < 23000) {
        this.data.filter(x => x.name === '22000 to 2999 pln').map(y => y.value += 1);
      } else if (post.salary >= 23000 && post.salary < 24000) {
        this.data.filter(x => x.name === '23000 to 23999 pln').map(y => y.value += 1);
      } else if (post.salary >= 24000 && post.salary < 25000) {
        this.data.filter(x => x.name === '24000 to 24999 pln').map(y => y.value += 1);
      } else if (post.salary >= 25000) {
        this.data.filter(x => x.name === 'More than 25000 pln').map(y => y.value += 1);
      }
    });
  }

  charContractType() {
    this.data = [];
    const uniqueStack = new Set(this.posts.map(post => post.contract_type));

    uniqueStack.forEach(contractType => {
      this.data.push(new HorizontalBar(contractType, 0));
    });

    this.posts.forEach(post => {
      this.data.filter(x => x.name === post.contract_type).map(y => y.value += 1);
    });
    this.data.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

  chartLocation() {
    this.data = [
      new HorizontalBar('Other', 0),
      new HorizontalBar('Śląsk', 0),
      new HorizontalBar('Trójmiasto', 0)
    ];

    const uniqueStack = new Set(this.posts.map(post => post.location));

    uniqueStack.forEach(location => {
      if (location.indexOf('Trójmiasto') < 0 && location.indexOf('Śląsk') < 0 && location.indexOf('Other') < 0) {
        this.data.push(new HorizontalBar(location, 0));
      }
    });

    this.posts.forEach(post => {
      if (post.location.indexOf('Trójmiasto') >= 0) {
        this.data.filter(x => x.name === 'Trójmiasto').map(y => y.value += 1);
      } else if (post.location.indexOf('Śląsk') >= 0) {
        this.data.filter(x => x.name === 'Śląsk').map(y => y.value += 1);
      } else if (post.location.indexOf('Other') >= 0) {
        this.data.filter(x => x.name === 'Other').map(y => y.value += 1);
      } else {
        this.data.filter(x => x.name === post.location).map(y => y.value += 1);
      }
    });
    this.data.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

}
