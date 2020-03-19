import {Component, Input} from '@angular/core';
import {Pie} from '../../models/pie.class';
import {environment} from '../../../environments/environment';

@Component({
  selector: 'app-pie',
  templateUrl: './pie.component.html',
  styleUrls: ['./pie.component.css']
})
export class PieComponent {

  @Input() data: Pie[];
  view: any[] = environment.view;
  gradient = false;
  showLegend = false;
  showLabels = true;
  isDoughnut = false;
  trimLabels = false;
  colorScheme = environment.colorScheme;

}
